from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_get_user_response
from clients.users.users_schema import GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from http import HTTPStatus 
import pytest

@pytest.mark.regression
@pytest.mark.users
def test_get_user_me(private_users_client, function_user):
    create_user_response = function_user.response
    get_user_response = private_users_client.get_user_me_api()
    get_user_response_data = GetUserResponseSchema.model_validate_json(get_user_response.text)
    
    assert_status_code(get_user_response.status_code, HTTPStatus.OK)
    assert_get_user_response(get_user_response_data.user, create_user_response.user)

    validate_json_schema(get_user_response.json(), get_user_response_data.model_json_schema())