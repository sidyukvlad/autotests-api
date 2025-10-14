from typing import TypedDict
from httpx import Client
from functools import lru_cache
from clients.authentification.authentification_client import get_authentification_client
from clients.authentification.authentification_schema import LoginRequestSchema
from pydantic import BaseModel


class AuthenticationUserSchema(BaseModel, frozen=True):
    email: str
    password: str


@lru_cache(maxsize=None)
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    authentification_client = get_authentification_client()
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentification_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response.token.access_token}"},
    )