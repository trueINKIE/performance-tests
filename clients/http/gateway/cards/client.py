from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class CardDict(TypedDict):
    """
    Описание структуры карты.
    """
    id: str
    pin: str
    cvv: str
    type: str
    status: str
    accountId: str
    cardNumber: str
    cardHolder: str
    expiryDate: str
    paymentSystem: str


class IssueVirtualCardRequestDict(TypedDict):
    """
    Структура данных для создания новой виртуальной карты.
    """
    userId: str
    accountId: str


class IssueVirtualCardResponseDict(TypedDict):
    """
    Описание структуры ответа выпуска виртуальной карты.
    """
    card: CardDict


class IssuePhysicalCardRequestDict(TypedDict):
    """
    Структура данных для создания новой физической карты.
    """
    userId: str
    accountId: str


class IssuePhysicalCardResponseDict(TypedDict):
    """
    Описание структуры ответа выпуска физической карты.
    """
    card: CardDict


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def issue_virtual_card_api(self, request: IssueVirtualCardRequestDict) -> Response:
        """
        Создание новой виртуальной карты.

        :param request: Словарь с данными новой виртуальной карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssuePhysicalCardRequestDict) -> Response:
        """
        Создание новой физической карты.

        :param request: Словарь с данными новой физической карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponseDict:
        """
        Создание новой виртуальной карты.

        :param account_id: Идентификатор счёта
        :param user_id: Идентификатор пользователя
        :return: Ответ от сервера (объект IssueVirtualCardResponseDict).
        """
        request = IssueVirtualCardRequestDict(userId=user_id, accountId=account_id)
        response = self.issue_virtual_card_api(request)
        return response.json()

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponseDict:
        """
        Создание новой физической карты.

        :param account_id: Идентификатор счёта
        :param user_id: Идентификатор пользователя
        :return: Ответ от сервера (объект IssuePhysicalCardResponseDict).
        """
        request = IssuePhysicalCardRequestDict(userId=user_id, accountId=account_id)
        response = self.issue_physical_card_api(request)
        return response.json()


def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:
    """
    Функция создаёт экземпляр CardsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CardsGatewayHTTPClient.
    """
    return CardsGatewayHTTPClient(client=build_gateway_http_client())