import httpx

payload = {"email": "user@example.com", "password": "string"}

login_response = httpx.post(
    "http://localhost:8000/api/v1/authentication/login", json=payload
)

login_response_data = login_response.json()

token = login_response_data["token"]["accessToken"]
headers = {"Authorization": f"Bearer {token}"}
me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

assert me_response.json() is not None
assert me_response.status_code == 200
print(me_response.json())
print(me_response.status_code)
