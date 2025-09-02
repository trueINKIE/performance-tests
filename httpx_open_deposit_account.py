import time

import httpx

client = httpx.Client(base_url="http://localhost:8003/api/v1")

create_user_data = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "Test",
    "firstName": "User",
    "middleName": "Account",
    "phoneNumber": "+78634626"
}

create_user_response = client.post(url="/users", json=create_user_data)
create_user_response_data = create_user_response.json()
create_user_id = create_user_response_data['user']['id']

open_deposit_account_data = {
    "userId": create_user_id
}

open_deposit_account_response = client.post(url="/accounts/open-deposit-account", json=open_deposit_account_data)

print(open_deposit_account_response.json())
print(open_deposit_account_response.status_code)