import ZagreusBank.Version2.custom_exceptions as errors
from ZagreusBank.Version2.data_access_layer.implementation_classes.Account_dao_imp import AccountDAOImp
from ZagreusBank.Version2.entities.Account import Account
from ZagreusBank.Version2.service_layer.abstract_services.Account_service import AccountService

"""
we are going to make use of dependency injection with our service class. This allows us to easily change the
implementation of our code by switching out the implementing class. Switching from a local to a cloud based database?
just pass in a cloud based implementation object into the service layer instead of a local based implementation object
"""


# BUSINESS LOGIC: accounts should have unique account numbers for the same customer

class AccountServiceImp(AccountService):
    def __init__(self, account_dao):
        # we are doing dependency injection with this init dunder method
        self.account_dao: AccountDAOImp = account_dao

    def service_create_account_entry(self, account: Account) -> Account:
        # need to implement business logic
        for current_account in self.account_dao.account_list:
            if current_account.customer_id == account.customer_id and current_account.account_id == account.account_id:
                raise errors.DuplicateAccountNumberException("Account could not be created: DUPLICATE ACCOUNT NUMBER")
            else:
                return self.account_dao.create_account_entry(account)

    def service_get_account_information(self, account_id: int) -> Account:
        return self.account_dao.get_account_information(account_id)

    def service_get_all_accounts_information(self) -> list[Account]:
        return self.account_dao.get_all_accounts_information()

    def service_update_account_information(self, account: Account) -> Account:
        for current_account in self.account_dao.account_list:
            if current_account.customer_id == account.customer_id:
                if current_account.account_id != account.account_id:
                    raise errors.DuplicateAccountNumberException("Account already exists")
        return self.account_dao.update_account_information(account)

    def service_delete_account_information(self, account_id: int) -> bool:
        return self.account_dao.delete_account_information(account_id)
