from clients.users.public_users_client import PublicUserClient
from clients.users.private_users_client import PrivateUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake
from fixtures.users import UserFixture
from http import HTTPStatus
import pytest


@pytest.mark.users
@pytest.mark.regression
class TestUsers:
    @pytest.mark.parametrize("domain", ["mail.ru", "gmail.com", "example.com"])
    def test_create_user(self, domain: str, public_users_client: PublicUserClient):
        request = CreateUserRequestSchema(
            email=fake.email(domain=domain)
        )
        response = public_users_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())
    
    def test_get_user_me(
            self, 
            private_users_client: PrivateUsersClient, 
            function_user: UserFixture
        ):
        create_user_response = function_user.response
        get_user_response = private_users_client.get_user_me_api()
        get_user_response_data = GetUserResponseSchema.model_validate_json(
            get_user_response.text)

        assert_status_code(get_user_response.status_code, HTTPStatus.OK)
        assert_get_user_response(
            get_user_response_data.user, create_user_response.user)

        validate_json_schema(get_user_response.json(),
                            get_user_response_data.model_json_schema())