import uuid
from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserRequestSchema(BaseModel):
    """
    Описание запроса на создание пользователя.
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema
