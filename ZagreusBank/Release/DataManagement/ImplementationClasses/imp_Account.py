import ZagreusBank.Release.DataManagement.DataAccessClasses.dao_Account as d_Acc
# import ZagreusBank.Release.DataManagement.DataAccessClasses.dao_Account


class imp_Account(d_Acc.dao_Account):
    account_data = "beans"
    account = d_Acc.Account(account_data)

    def on_hold(self) -> bool:
        pass

    def update_balance(self, account_number: int, updated_balance: float):
        pass

    def withdraw(self, account_number: int, withdraw_amount: float):
        pass

    def close_account(self, account_number: int):
        pass