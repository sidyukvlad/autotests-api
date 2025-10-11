from clients.users.public_users_client import get_public_users_client, PublicUserClient
from clients.authentification.authentification_client import get_authentification_client, AuthentificationClient
from clients.users.users_schema import CreateUserRequestSchema
from clients.authentification.authentification_schema import LoginRequestSchema, LoginResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.authentication import assert_login_response
from tools.assertions.schema import validate_json_schema
from http import HTTPStatus
from tests.conftest import UserFixture
import pytest


@pytest.mark.regression
@pytest.mark.authentication
def test_login(function_user: UserFixture, authentification_client: AuthentificationClient):

    request = LoginRequestSchema(
        email=function_user.email,
        password=function_user.password,
    )

    response = authentification_client.login_api(
        request
    )
    response_data = LoginResponseSchema.model_validate_json(
        response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_login_response(response_data)

    validate_json_schema(response.json(),
                         response_data.model_json_schema())
