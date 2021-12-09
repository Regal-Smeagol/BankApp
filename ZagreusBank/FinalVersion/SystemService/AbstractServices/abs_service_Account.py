from abc import abstractmethod, ABC
from ZagreusBank.Release.DataManagement.DataClasses.Account import Account


class abs_service_Account(ABC):

    @abstractmethod
    def service_create_account(self, new_account: Account) -> Account:
        pass

    @abstractmethod
    def service_update_account_information(self, account: Account) -> Account:
        pass

    @abstractmethod
    def service_get_account_information(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def service_get_all_account_information(self) -> list[Account]:
        pass

    @abstractmethod
    def service_get_accounts_by_customer_id(self, customer_id: int) -> list[Account]:
        pass

    @abstractmethod
    def service_close_account(self, account_number: int) -> bool:
        pass

    @abstractmethod
    def service_withdraw_from_account(self, account: Account) -> float:
        pass

    @abstractmethod
    def service_transfer_between_accounts(self) -> list[Account]:
        pass

    @abstractmethod
    def service_deposit_into_account(self):