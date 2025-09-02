from httpx import QueryParams, Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import GetOperationsQuerySchema, GetOperationsSummaryQuerySchema, \
    MakeOperationRequestSchema, MakePurchaseOperationRequestSchema, GetOperationResponseSchema, \
    GetOperationReceiptResponseSchema, GetOperationsResponseSchema, OperationsSummaryResponseSchema, \
    MakeFeeOperationResponseSchema, MakeTopUpOperationResponseSchema, MakeCashBackOperationResponseSchema, \
    MakeTransferOperationResponseSchema, MakePurchasesOperationResponseSchema, MakeBillPaymentOperationResponseSchema, \
    MakeCashWithdrawalOperationResponseSchema, MakeCashWithdrawalOperationRequestSchema, \
    MakeBillPaymentOperationRequestSchema, MakeTransferOperationRequestSchema, MakeCashBackOperationRequestSchema, \
    MakeTopUpOperationRequestSchema, MakeFeeOperationRequestSchema


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

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Выполняет GET-запрос на получение списка операций счета.

        :param query: Словарь с параметрами запроса, например: {'account_id': '123'}.
        :return: Объект httpx.Response с данными о счетах.
        """
        return self.get(url="/api/v1/operations", params=QueryParams(**query.model_dump(by_alias=True)))

    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
        Выполняет GET-запрос на получение статистики по операциям счета.

        :param query: Словарь с параметрами запроса, например: {'account_id': '123'}.
        :return: Объект httpx.Response с данными о счетах.
        """
        return self.get(url="/api/v1/operations/operations-summary", params=QueryParams(**query.model_dump(by_alias=True)))

    def make_fee_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param request: Словарь с параметрами запроса.
        :return: Объект httpx.Response.
        """
        return self.post(url="/api/v1/operations/make-fee-operation", json=request.model_dump(by_alias=True))

    def make_top_up_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции пополнения.

        :param request: Словарь с параметрами запроса.
        :return: Объект httpx.Response.
        """
        return self.post(url="/api/v1/operations/make-top-up-operation", json=request.model_dump(by_alias=True))

    def make_cashback_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param request: Словарь с параметрами запроса.
        :return: Объект httpx.Response.
        """
        return self.post(url="/api/v1/operations/make-cashback-operation", json=request.model_dump(by_alias=True))

    def make_transfer_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции перевода.

        :param request: Словарь с параметрами запроса.
        :return: Объект httpx.Response.
        """
        return self.post(url="/api/v1/operations/make-transfer-operation", json=request.model_dump(by_alias=True))

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param request: Словарь с параметрами запроса.
        :return: Объект httpx.Response.
        """
        return self.post(url="/api/v1/operations/make-purchase-operation", json=request.model_dump(by_alias=True))

    def make_bill_payment_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты по счету.

        :param request: Словарь с параметрами запроса.
        :return: Объект httpx.Response.
        """
        return self.post(url="/api/v1/operations/make-bill-payment-operation", json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции снятия наличных денег.

        :param request: Словарь с параметрами запроса.
        :return: Объект httpx.Response.
        """
        return self.post(url="/api/v1/operations/make-cash-withdrawal-operation", json=request.model_dump(by_alias=True))

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        response = self.get_operation_api(operation_id=operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        response = self.get_operation_receipt_api(operation_id=operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        query = GetOperationsQuerySchema(
            account_id=account_id
        )
        response = self.get_operations_api(query=query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> OperationsSummaryResponseSchema:
        query = GetOperationsSummaryQuerySchema(
            account_id=account_id
        )
        response = self.get_operations_summary_api(query=query)
        return OperationsSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
        request = MakeFeeOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseSchema:
        request = MakeTopUpOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashBackOperationResponseSchema:
        request = MakeCashBackOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cashback_operation_api(request)
        return MakeCashBackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseSchema:
        request = MakeTransferOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchasesOperationResponseSchema:
        request = MakePurchaseOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            card_id=card_id,
            account_id=account_id,
            category="Taxi"
        )
        response = self.make_purchase_operation_api(request)
        return MakePurchasesOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseSchema:
        request = MakeBillPaymentOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseSchema:
        request = MakeCashWithdrawalOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())