from locust import task, User, between

from clients.grpc.gateway.locust import GatewayGRPCTaskSet
from contracts.services.accounts.rpc_get_accounts_pb2 import GetAccountsResponse
from contracts.services.gateway.accounts.rpc_open_deposit_account_pb2 import OpenDepositAccountResponse


class GetAccountsTaskSet(GatewayGRPCTaskSet):
    external_user_id: str | None = None
    open_deposit_account_response: OpenDepositAccountResponse | None = None
    get_accounts_response: GetAccountsResponse | None = None

    @task(2)
    def create_user(self):
        self.external_user_id = self.users_gateway_client.create_user().user.id

    @task(2)
    def open_deposit_account(self):
        if not self.external_user_id:
            return

        self.open_deposit_account_response = self.accounts_gateway_client.open_deposit_account(
            user_id=self.external_user_id
        )

    @task(6)
    def get_accounts(self):
        if not self.external_user_id:
            return

        self.get_accounts_response = self.accounts_gateway_client.get_accounts(
            user_id=self.external_user_id
        )


class GetAccountsScenarioUser(User):
    host = "localhost"
    tasks = [GetAccountsTaskSet]
    wait_time = between(1, 3)