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
create_user_id = create_user_response_data['user']["id"]

open_credit_card_account_data = {
    "userId": create_user_id
}

open_credit_card_account_response = client.post(url="/accounts/open-credit-card-account", json=open_credit_card_account_data)
open_credit_card_account_response_data = open_credit_card_account_response.json()
open_credit_card_account_id = open_credit_card_account_response_data['account']['id']
open_credit_card_card_id = open_credit_card_account_response_data['account']['cards'][0]['id']

make_purchase_operation_data = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "category": "taxi",
    "cardId": open_credit_card_card_id,
    "accountId": open_credit_card_account_id
}

make_purchase_operation_response = client.post(url="/operations/make-purchase-operation", json=make_purchase_operation_data)
make_purchase_operation_response_data = make_purchase_operation_response.json()
make_purchase_operation_id = make_purchase_operation_response_data['operation']['id']

operation_receipt_response = client.get(url=f'operations/operation-receipt/{make_purchase_operation_id}')
operation_receipt_response_data = operation_receipt_response.json()

print(operation_receipt_response_data)