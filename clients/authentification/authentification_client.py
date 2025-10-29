from httpx import Response
from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.authentification.authentification_schema import LoginRequestSchema, RefreshRequestSchema, LoginResponseSchema
import allure
from tools.routes import APIRoutes


class AuthentificationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """
    @allure.step("Authentification user")
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            f"{APIRoutes.AUTHENTICATION}/login",
            json=request.model_dump(by_alias=True)
        )
    
    @allure.step("Refresh authentification token")
    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            f"{APIRoutes.AUTHENTICATION}/refresh",
            json=request.model_dump(by_alias=True)
        )

    # Добавили метод login
    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)  # Отправляем запрос на аутентификацию
        return LoginResponseSchema.model_validate_json(response.text)


def get_authentification_client() -> AuthentificationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthentificationClient(client=get_public_http_client())