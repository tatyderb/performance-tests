from pydantic import BaseModel, Field, EmailStr, ConfigDict
from pydantic.alias_generators import to_camel


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

    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str
    phone_number: str


# Добавили суффикс Schema вместо Dict
class CreateUserResponseSchema(BaseModel):  # Наследуем от BaseModel вместо TypedDict
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema
