import time
from typing import TypedDict

from httpx import Response, request

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class CreateUserRequestDict(TypedDict):
    """
    Структура данных для создания нового пользователя.
    """
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class UserDict(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class GetUserResponseDict(TypedDict):
    """
    Описание структуры ответа получения пользователя.
    """
    user: UserDict


class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserDict


class UsersGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/users сервиса http-gateway.
    """

    def get_user_api(self, user_id: str) -> Response:
        """
        Получить данные пользователя по его user_id.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/users/{user_id}")

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Создание нового пользователя.

        :param request: Словарь с данными нового пользователя.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/users", json=request)

    def get_user(self, user_id: str) -> GetUserResponseDict:
        """
        Получить данные пользователя по его user_id.

        :return: Ответ от сервера (объект GetUserResponseDict).
        """
        response = self.get_user_api(user_id)
        return response.json()

    def create_user(self) -> CreateUserResponseDict:
        """
        Создание нового пользователя.

        :return: Ответ от сервера (объект CreateUserResponseDict).
        """
        request = CreateUserRequestDict(
            email=f"user.{time.time()}@example.com",
            lastName="string",
            firstName="string",
            middleName="string",
            phoneNumber="string"
        )
        response = self.create_user_api(request)
        return response.json()


def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    """
    Функция создаёт экземпляр UsersGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию UsersGatewayHTTPClient.
    """
    return UsersGatewayHTTPClient(client=build_gateway_http_client())