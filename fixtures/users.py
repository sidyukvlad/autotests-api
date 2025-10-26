from clients.users.public_users_client import get_public_users_client, PublicUserClient
from clients.users.private_users_client import get_private_users_client, PrivateUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from clients.private_http_builder import AuthenticationUserSchema

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
    
    @property
    def authentification_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(email=self.email, password=self.password)


@pytest.fixture
def public_users_client() -> PublicUserClient:
    return get_public_users_client()


@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivateUsersClient:
    return get_private_users_client(function_user.authentification_user)


@pytest.fixture
def function_user(public_users_client: PublicUserClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)


@pytest.fixture(scope="class")
def class_user(public_users_client: PublicUserClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)