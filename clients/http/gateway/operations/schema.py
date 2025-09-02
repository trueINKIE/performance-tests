from datetime import datetime
from enum import StrEnum
from pydantic import BaseModel, Field, ConfigDict, HttpUrl
from tools.fakers import fake


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(BaseModel):
    """
    Описание структуры операции.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: str
    status: str
    amount: float
    category: str
    card_id: str = Field(alias="cardId")
    created_at: datetime = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationReceiptSchema(BaseModel):
    """
    Описание структуры чека операции.
    """
    url: HttpUrl
    document: str


class OperationsSummarySchema(BaseModel):
    """
    Описание структуры статистики счёта.
    """
    model_config = ConfigDict(populate_by_name=True)

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class OperationsSummaryResponseSchema(BaseModel):
    """
    Описание структуры ответа получения статистики счёта.
    """
    summary: OperationsSummarySchema


class GetOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа получения операции.
    """
    operation: OperationSchema


class GetOperationsResponseSchema(BaseModel):
    """
    Описание структуры ответа получения списка операций по счёту.
    """
    operations: list[OperationSchema]


class GetOperationReceiptResponseSchema(BaseModel):
    """
    Описание структуры ответа получения чека операций.
    """
    receipt: OperationReceiptSchema


class MakeFeeOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции комиссии.
    """
    operation: OperationSchema


class MakeFeeOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции комиссии.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=lambda: fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции пополнения.
    """
    operation: OperationSchema


class MakeTopUpOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции пополнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=lambda: fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeCashBackOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции кэшбэк.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=lambda: fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeCashBackOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции кэшбэка.
    """
    operation: OperationSchema


class MakeTransferOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции перевода.
    """
    operation: OperationSchema


class MakePurchasesOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции покупки.
    """
    operation: OperationSchema


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции оплаты по счёту.
    """
    operation: OperationSchema


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции снятия наличных.
    """
    operation: OperationSchema


class MakeCashWithdrawalOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции снятия наличных.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=lambda: fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeBillPaymentOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции оплаты по счёту.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=lambda: fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeTransferOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции перевода.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=lambda: fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class GetOperationsQuerySchema(BaseModel):
    """
    Структура данных для получения списка операций счёта.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура данных для получения статистики по операциям счёта.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class MakeOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=lambda: fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции покупки.
    """
    category: str = Field(alias="lastName", default_factory=fake.category())