import httpx
from tools.fakers import fake

email = fake.email()

create_user_payload = {
    "email": email,
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)
# assert create_user_response.status_code == 200

login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

assert create_user_response.status_code == 200

update_user_payload = {
    "email": fake.email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

user_id = create_user_response_data["user"]["id"]
patch_user_headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
update_response = httpx.patch(
    f'http://localhost:8000/api/v1/users/{user_id}',
    json=update_user_payload,
    headers = patch_user_headers
)
update_response_data = update_response.json()

print('Update user data:', update_response_data)
print(update_response.status_code)




