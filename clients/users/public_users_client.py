from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUserClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Метод создает пользователя.

        :param request: Словарь с полями нового пользователя
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            "/api/v1/users",
            json=request.model_dump(by_alias=True)
        )

    # Добавили новый метод
    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        print(response.json())
        return CreateUserResponseSchema.model_validate_json(response.text)


# Добавляем builder для PublicUsersClient
def get_public_users_client() -> PublicUserClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUserClient(client=get_public_http_client())