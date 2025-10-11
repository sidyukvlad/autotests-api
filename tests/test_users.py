from clients.users.public_users_client import get_public_users_client, PublicUserClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from http import HTTPMethod, HTTPStatus
from tools.assertions.base import assert_status_code, assert_equal
from tools.assertions.users import assert_create_user_response
from tools.assertions.schema import validate_json_schema
import pytest

@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_users_client: PublicUserClient):
    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_create_user_response(request, response_data)

    validate_json_schema(response.json(), response_data.model_json_schema())
    
