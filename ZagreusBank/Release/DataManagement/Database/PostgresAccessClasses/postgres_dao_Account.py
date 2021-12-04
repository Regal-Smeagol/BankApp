from ZagreusBank.Release.DataManagement.DataAccessClasses.dao_Account import dao_Account
from

class postgres_Account(dao_Account):
    def on_hold(self, account_id: int) -> bool:
        sql_server_request = "select * from hold where account_id = %s"


    def update_balance(self, account_number: int, updated_balance: float):
        pass

    def withdraw(self, account_number: int, withdraw_amount: float):
        pass

    def close_account(self, account_number: int):
        pass