import httpx

# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
#
# print(response.status_code)  # 200
# print(response.json())
#
# data = {
#     "title": "Новая задача",
#     "completed": False,
#     "userId": 1
# }
#
# response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
#
# print(response.status_code)  # 201 (Created)
# print(response.json())

headers = {"Authorization": "Bearer my_secret_token"}

response = httpx.get("https://httpbin.org/get", headers=headers)

# print(response.json())


files = {"file": ("example.txt", open("example.txt", "rb"))}

# response = httpx.post("https://httpbin.org/post", files=files)

# print(response.json())  # Ответ с данными о загруженном файле

# import httpx

with httpx.Client(headers={"Authorization": "Bearer my_secret_token"}) as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

# print(response1.json())  # Данные первой задачи
# print(response2.json())

# try:
#     response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
#     response.raise_for_status()  # Вызовет исключение при 4xx/5xx
# except httpx.HTTPStatusError as e:
#     print(f"Ошибка запроса: {e}")

# response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
# response.raise_for_status()
# print(response.status_code)

try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")
