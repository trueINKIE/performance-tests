from typing import Any, TypedDict

from httpx import Client, URL, Response, QueryParams


class HTTPClientExtension(TypedDict, total=False):
    route: str


class HTTPClientExtensions(TypedDict, total=False):
    route: str


class HTTPClient:
    """
    Базовый HTTP API клиент, принимающий объект httpx.Client.

    :param client: экземпляр httpx.Client для выполнения HTTP-запросов
    """

    def __init__(self, client: Client) -> None:
        self.client = client

    def get(
            self,
            url: str | URL,
            params: QueryParams | None = None,
            extensions: HTTPClientExtensions | None = None
    ) -> Response:
        """
        Выполняет GET-запрос.

        :param url: URL-адрес эндпоинта.
        :param params: GET-параметры запроса (например, ?key=value).
        :param extensions: Дополнительные данные, передаваемые через HTTPX extensions.
        :return: Объект Response с данными ответа.
        """
        return self.client.get(url=url, params=params, extensions=extensions)

    def post(
            self,
            url: str | URL,
            json: Any | None = None,
            extensions: HTTPClientExtensions | None = None
    ) -> Response:
        """
        Выполняет POST-запрос.

        :param url: URL-адрес эндпоинта.
        :param json: Данные в формате JSON.
        :param extensions: Дополнительные данные, передаваемые через HTTPX extensions.
        :return: Объект Response с данными ответа.
        """
        return self.client.post(url=url, json=json, extensions=extensions)