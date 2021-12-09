from abc import abstractmethod, ABC
from ZagreusBank.Release.DataManagement.DataClasses.Account import Account as Account


class dao_Account(ABC, Account):

    @abstractmethod
    def create_account(self, new_account: Account) -> Account:
        pass

    @abstractmethod
    def update_account_information(self, account: Account) -> Account:
        pass

    @abstractmethod
    def get_account_information(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def get_accounts_by_customer_id(self, customer_id: int) -> list[Account]:
        pass

    @abstractmethod
    def deposit_into_account(self, account: Account, deposit_amount: float) -> bool:
        pass

    @abstractmethod
    def withdraw_from_account(self, account: Account, withdraw_amount: float) -> bool:
        pass

    @abstractmethod
    def transfer_between_accounts(self, send_account_id: int, receive_account_id: int, transfer_amount: float) -> bool:
        pass

    @abstractmethod
    def close_account(self, account_number: int) -> bool:
        pass
