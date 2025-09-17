import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()


client = httpx.Client(
    base_url="http://localhost:8000",
    timeout=100  # Таймаут в секундах
)


response = client.get("/api/v1/users/me")
print(response.text)


response = client.get("/api/v1/users/me")

print(response.text)