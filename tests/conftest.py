from clients.authentification.authentification_client import get_authentification_client, AuthentificationClient
from clients.users.public_users_client import get_public_users_client, PublicUserClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from pydantic import BaseModel, EmailStr
import pytest


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email
    
    @property
    def password(self) -> str:
        return self.request.password


@pytest.fixture
def authentification_client() -> AuthentificationClient:
    return get_authentification_client()


@pytest.fixture
def public_users_client() -> PublicUserClient:
    return get_public_users_client()


@pytest.fixture
def function_user(public_users_client: PublicUserClient):
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)


@pytest.fixture(scope="class")
def class_user(public_users_client: PublicUserClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)