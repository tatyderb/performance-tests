from pydantic import BaseModel, EmailStr, ConfigDict
from pydantic.alias_generators import to_camel

class CreateUserRequestSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, validate_by_alias=True)
    email: EmailStr  # Используем EmailStr вместо str
    last_name: str
    first_name: str
    middle_name: str
    phone_number: str

class UserSchema(CreateUserRequestSchema):
    id: str

class CreateUserResponseSchema(BaseModel):
    user: UserSchema

create_user_dict = {
  "email": "user@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}
user_dict = {
  "id": "string",
  "email": "user@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}
create_user_response_dict = {
  "user": {
    "id": "string",
    "email": "user@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
  }
}

create_user_model = CreateUserRequestSchema(**create_user_dict)
print(f'{create_user_model=}')

user_model = UserSchema(**user_dict)
print(f'{user_model=}')

create_user_response_model = CreateUserResponseSchema(**create_user_response_dict)
print(f'{create_user_response_model=}')
print(create_user_response_model.model_dump(by_alias=True))

print('-----------------')
text='{"user":{"id":"418f4ba6-9a59-4fbc-8a36-4f9886c3c6a5","email":"user.1769283774.6198812@example.com","lastName":"string","firstName":"string","middleName":"string","phoneNumber":"string"}}'
create_user_response_model = CreateUserResponseSchema.model_validate_json(text)
print(f'{create_user_response_model=}')
print(create_user_response_model.model_dump(by_alias=True))

