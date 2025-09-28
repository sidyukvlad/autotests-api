from clients.users.public_users_client import get_public_users_client
from clients.users.private_users_client import get_private_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.fakers import get_random_email
import jsonschema
from pprint import pprint
from tools.assertions.schema import validate_json_schema

public_users_client = get_public_users_client()
private_users_client = get_private_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

create_user_response = public_users_client.create_user(create_user_request)
print(create_user_response.user.id)

get_user_response = private_users_client.get_user(create_user_response.user.id)


create_user_response_schema = CreateUserResponseSchema.model_json_schema()