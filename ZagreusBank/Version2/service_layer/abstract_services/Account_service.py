from abc import ABC, abstractmethod

from ZagreusBank.Version2.entities.Account import Account


class AccountService(ABC):

    # create account method
    @abstractmethod
    def service_create_account_entry(self, account: Account) -> Account:
        pass

    # get account information
    @abstractmethod
    def service_get_account_information(self, account_id: int) -> Account:
        pass

    # get all account information
    @abstractmethod
    def service_get_all_accounts_information(self) -> list[Account]:
        pass

    # update account information
    @abstractmethod
    def service_update_account_information(self, account: Account) -> Account:
        pass

    # delete account information
    @abstractmethod
    def service_delete_account_information(self, account_id: int) -> bool:
        pass