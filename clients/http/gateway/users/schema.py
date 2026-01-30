from pydantic import BaseModel, Field, EmailStr, ConfigDict
from pydantic.alias_generators import to_camel

from tools.fakers import fake


# Добавили суффикс Schema вместо Dict
class UserSchema(BaseModel):  # Наследуем от BaseModel вместо TypedDict
    """
    Описание структуры пользователя.
    """
    model_config = ConfigDict(alias_generator=to_camel, validate_by_alias=True)
    id: str
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str
    phone_number: str


# Добавили суффикс Schema вместо Dict
class GetUserResponseSchema(BaseModel):  # Наследуем от BaseModel вместо TypedDict
    """
    Описание структуры ответа получения пользователя.
    """
    user: UserSchema


# Добавили суффикс Schema вместо Dict
class CreateUserRequestSchema(BaseModel):  # Наследуем от BaseModel вместо TypedDict
    """
    Структура данных для создания нового пользователя.
    """
    model_config = ConfigDict(alias_generator=to_camel, validate_by_alias=True, validate_by_name=True)

    email: EmailStr = Field(default_factory=fake.email)
    last_name: str = Field(default_factory=fake.last_name)
    first_name: str = Field(default_factory=fake.first_name)
    middle_name: str = Field(default_factory=fake.middle_name)
    phone_number: str = Field(default_factory=fake.phone_number)


# Добавили суффикс Schema вместо Dict
class CreateUserResponseSchema(BaseModel):  # Наследуем от BaseModel вместо TypedDict
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema
