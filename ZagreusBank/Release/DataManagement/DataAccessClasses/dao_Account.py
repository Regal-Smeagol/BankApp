from abc import abstractmethod, ABC
from ZagreusBank.Release.DataManagement.DataClasses.Account import Account


class dao_Account(ABC, Account):

    @abstractmethod
    def on_hold(self) -> bool:
        pass

    @abstractmethod
    def update_balance(self, account_number: int, updated_balance: float):
        pass

    @abstractmethod
    def withdraw(self, account_number: int, withdraw_amount: float):
        pass

    @abstractmethod
    def close_account(self, account_number: int):
        pass
