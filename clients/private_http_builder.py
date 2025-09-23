from typing import TypedDict

from httpx import Client

from clients.authentification.authentification_client import get_authentification_client, LoginRequestDict


class AuthenticationUserDict(TypedDict):
    email: str
    password: str


def get_private_http_client(user: AuthenticationUserDict) -> Client:
    authentification_client = get_authentification_client()

    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    login_response = authentification_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response['token']['accessToken']}"},
    )