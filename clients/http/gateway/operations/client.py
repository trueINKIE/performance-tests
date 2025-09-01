from typing import TypedDict

from httpx import QueryParams, Response

from clients.http.client import HTTPClient


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