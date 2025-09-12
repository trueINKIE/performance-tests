from fastapi import FastAPI, APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr, RootModel

app = FastAPI()

courses_router = APIRouter(
    prefix="/api/v1/courses",
    tags=["courses-service"]
)


class CourseIn(BaseModel):
    """
    Модель для приёма входных данных (создание и обновление курса).
    """
    title: str
    max_score: int
    min_score: int
    description: str


class CourseOut(CourseIn):
    """
    Модель для отдачи данных о курсе, включая его ID.
    """
    id: int


class CourseStore(RootModel):
    """
    In-memory хранилище курсов вместо реальной БД.
    """
    root: list[CourseOut]

    def find(self, course_id: int) -> CourseOut | None:
        """
        Находит курс по ID.
        Возвращает CourseOut или None, если не найден.
        """
        return next(filter(lambda course: course.id == course_id, self.root), None)

    def create(self, course_in: CourseIn) -> CourseOut:
        """
        Создаёт новый курс, генерируя для него следующий ID.
        """
        course = CourseOut(id=len(self.root) + 1, **course_in.model_dump())
        self.root.append(course)
        return course

    def update(self, course_id: int, course_in: CourseIn) -> CourseOut:
        """
        Обновляет существующий курс по ID.
        """
        index = next(index for index, course in enumerate(self.root) if course.id == course_id)
        updated = CourseOut(id=course_id, **course_in.model_dump())
        self.root[index] = updated
        return updated

    def delete(self, course_id: int) -> None:
        """
        Удаляет курс по ID, фильтруя список.
        """
        self.root = [course for course in self.root if course.id != course_id]


store = CourseStore(root=[])


@courses_router.get("/{course_id}", response_model=CourseOut)
async def get_course(course_id: int):
    """
    GET /api/v1/courses/{course_id}
    Возвращает курс по ID или 404, если не найден.
    """
    if not (course := store.find(course_id)):
        raise HTTPException(
            detail=f"Course with id {course_id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )

    return course


@courses_router.get("", response_model=list[CourseOut])
async def get_courses():
    """
    GET /api/v1/courses
    Возвращает список всех курсов.
    """
    return store.root


@courses_router.post("", response_model=CourseOut, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseIn):
    """
    POST /api/v1/courses
    Создаёт новый курс и возвращает его данные с ID.
    """
    return store.create(course)


@courses_router.put("/{course_id}", response_model=CourseOut)
async def update_course(course_id: int, course: CourseIn):
    """
    PUT /api/v1/courses/{course_id}
    Обновляет данные курса по ID или возвращает 404, если не существует.
    """
    if not store.find(course_id):
        raise HTTPException(
            detail=f"Course with id {course_id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )

    return store.update(course_id, course)


@courses_router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: int):
    """
    DELETE /api/v1/courses/{course_id}
    Удаляет курс по ID или возвращает 404, если не существует.
    """
    if not store.find(course_id):
        raise HTTPException(
            detail=f"Courses with id {course_id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )

    store.delete(course_id)


app.include_router(courses_router)