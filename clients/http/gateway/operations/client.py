from datetime import datetime
from typing import TypedDict

from httpx import QueryParams, Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class OperationDict(TypedDict):
    """
    Описание структуры операции.
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: datetime
    accountId: str


class OperationReceiptDict(TypedDict):
    """
    Описание структуры чека операции.
    """
    url: str
    document: str


class OperationsSummaryDict(TypedDict):
    """
    Описание структуры статистики счёта.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class OperationsSummaryResponseDict(TypedDict):
    """
    Описание структуры ответа получения статистики счёта.
    """
    summary: OperationsSummaryDict


class GetOperationResponseDict(TypedDict):
    """
    Описание структуры ответа получения операции.
    """
    operation: OperationDict


class GetOperationsResponseDict(TypedDict):
    """
    Описание структуры ответа получения списка операций по счёту.
    """
    operations: list[OperationDict]


class GetOperationReceiptResponseDict(TypedDict):
    """
    Описание структуры ответа получения чека операций.
    """
    receipt: OperationReceiptDict


class MakeFeeOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции комиссии.
    """
    operation: OperationDict


class MakeFeeOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции комиссии.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeTopUpOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции пополнения.
    """
    operation: OperationDict


class MakeTopUpOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции пополнения.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeCashBackOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции кэшбэк.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeCashBackOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции кэшбэка.
    """
    operation: OperationDict


class MakeTransferOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции перевода.
    """
    operation: OperationDict


class MakePurchasesOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции покупки.
    """
    operation: OperationDict


class MakeBillPaymentOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции оплаты по счёту.
    """
    operation: OperationDict


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции снятия наличных.
    """
    operation: OperationDict


class MakeCashWithdrawalOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции снятия наличных.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeBillPaymentOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции оплаты по счёту.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeTransferOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции перевода.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения списка операций счёта.
    """
    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура данных для получения статистики по операциям счёта.
    """
    accountId: str


class MakeOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции покупки.
    """
    category: str


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение списка операций счёта.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response с данными о счетах.
        """
        return self.get(url=f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение чека операции.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response с данными о счетах.
        """
        return self.get(url=f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными о счетах.
        """
        return self.get(url="/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение статистики по операциям счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными о счетах.
        """
        return self.get(url="/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeOperationRequestDict):
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param request: Словарь с параметрами запроса.
        :return: Объект httpx.Response.
        """
        return self.post(url="/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeOperationRequestDict):
        """
        Выполняет POST-запрос для создания операции пополнения.

        :param request: Словарь с параметрами запроса.
        :return: Объект httpx.Response.
        """
        return self.post(url="/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeOperationRequestDict):
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param request: Словарь с параметрами запроса.
        :return: Объект httpx.Response.
        """
        return self.post(url="/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeOperationRequestDict):
        """
        Выполняет POST-запрос для создания операции перевода.

        :param request: Словарь с параметрами запроса.
        :return: Объект httpx.Response.
        """
        return self.post(url="/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict):
        """
        Выполняет POST-запрос для создания операции покупки.

        :param request: Словарь с параметрами запроса.
        :return: Объект httpx.Response.
        """
        return self.post(url="/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeOperationRequestDict):
        """
        Выполняет POST-запрос для создания операции оплаты по счету.

        :param request: Словарь с параметрами запроса.
        :return: Объект httpx.Response.
        """
        return self.post(url="/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeOperationRequestDict):
        """
        Выполняет POST-запрос для создания операции снятия наличных денег.

        :param request: Словарь с параметрами запроса.
        :return: Объект httpx.Response.
        """
        return self.post(url="/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id=operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        response = self.get_operation_receipt_api(operation_id=operation_id)
        return response.json()

    def get_operations(self, accountId: str) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(
            accountId=accountId
        )
        response = self.get_operations_api(query=query)
        return response.json()

    def get_operations_summary(self, accountId: str) -> OperationsSummaryResponseDict:
        query = GetOperationsSummaryQueryDict(
            accountId=accountId
        )
        response = self.get_operations_summary_api(query=query)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashBackOperationResponseDict:
        request = MakeCashBackOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchasesOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
            category="Taxi"
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())