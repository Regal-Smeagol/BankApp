from abc import abstractmethod, ABC
from ZagreusBank.Release.DataManagement.DataClasses.Account import Account


class dao_Account(ABC):

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
    def get_all_account_information(self) -> list[Account]:
        pass

    @abstractmethod
    def get_accounts_by_customer_id(self, customer_id: int) -> list[Account]:
        pass

    @abstractmethod
    def close_account(self, account_number: int) -> bool:
        pass
