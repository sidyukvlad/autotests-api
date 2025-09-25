from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = Field(alias="isActive")

user_data = {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "isActive": True,
}
user = User(**user_data)
# user = User(
#     id="1",
#     name="Alice",
#     email="alice@example.com",
#     is_active=True,
# )

print(user.model_dump())