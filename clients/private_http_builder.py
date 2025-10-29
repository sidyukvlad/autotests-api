from typing import TypedDict
from httpx import Client
from functools import lru_cache
from clients.authentification.authentification_client import get_authentification_client
from clients.authentification.authentification_schema import LoginRequestSchema
from pydantic import BaseModel
from clients.event_hooks import curl_event_hook
from config import settings

class AuthenticationUserSchema(BaseModel, frozen=True):
    email: str
    password: str


@lru_cache(maxsize=None)
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    authentification_client = get_authentification_client()
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentification_client.login(login_request)

    return Client(
        timeout=settings.http_client.timeout,
        base_url=settings.http_client.client_url,
        headers={"Authorization": f"Bearer {login_response.token.access_token}"},
        event_hooks={"request": [curl_event_hook]}
    )