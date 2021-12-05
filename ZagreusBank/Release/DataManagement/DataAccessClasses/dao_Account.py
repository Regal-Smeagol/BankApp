from abc import abstractmethod, ABC
from typing import List
from ZagreusBank.Release.DataManagement.DataClasses.Account import Account as Account


class dao_Account(ABC, Account):

    @abstractmethod
    def create_account(self, new_account: Account) -> Account:
        pass

    @abstractmethod
    def update_account_information(self, account: Account):
        pass

    @abstractmethod
    def is_on_hold(self, account_id: int) -> bool:
        pass

    @abstractmethod
    def get_account_information(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def get_accounts_by_customer_id(self, customer_id: int) -> List[Account]:
        pass

    @abstractmethod
    def close_account(self, account_number: int) -> bool:
        pass
