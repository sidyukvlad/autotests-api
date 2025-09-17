from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class UserRequestDict(TypedDict):
    """
    Описание запроса на создание пользователя.
    """

    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUserClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    def create_user_api(self, request: UserRequestDict) -> Response:
        """
        Метод создает пользователя.

        :param request: Словарь с полями нового пользователя
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)
