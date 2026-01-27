import time

from clients.http.gateway.users.client import build_users_gateway_http_client

# Инициализируем клиент UsersGatewayHTTPClient
users_gateway_client = build_users_gateway_http_client()

create_user_response = users_gateway_client.create_user()
print('Create user data:', create_user_response)

user_id = create_user_response.user.id

get_user_response = users_gateway_client.get_user(user_id=user_id)
print('Get user data:', get_user_response)

