from ZagreusBank.Version2 import custom_exceptions as errors
from ZagreusBank.Version2.data_access_layer.implementation_classes.Account_postgres_dao import AccountPostgresDAO
from ZagreusBank.Version2.entities.Account import Account
from ZagreusBank.Version2.service_layer.abstract_services.Account_service import AccountService


class AccountPostgresService(AccountService):
    def __init__(self, account_dao: AccountPostgresDAO):
        self.account_dao = account_dao

    # need to check and make sure accounts do not have the same account number
    def service_create_account_entry(self, account: Account) -> Account:
        accounts = self.account_dao.get_all_accounts_information()
        for existing_account in accounts:
            if existing_account.customer_id == account.customer_id:
                raise errors.DuplicateAccountNumberException("Account number is already taken!")
        created_account = self.account_dao.create_account_entry(account)
        return created_account

    def service_get_account_information(self, account_id: int) -> Account:
        return self.account_dao.get_account_information(account_id)

    def service_get_all_accounts_information(self) -> list[Account]:
        return self.account_dao.get_all_accounts_information()

    # need to check and make sure accounts do not have the same account number
    def service_update_account_information(self, account: Account) -> Account:
        accounts = self.account_dao.get_all_accounts_information()
        for current_account in accounts:
            if current_account.customer_id == account.customer_id:
                if current_account.account_id == account.account_id:
                    raise errors.DuplicateAccountNumberException("Account number is already taken!")
        updated_account = self.account_dao.update_account_information(account)
        return updated_account

    def service_delete_account_information(self, account_id: int) -> bool:
        return self.account_dao.delete_account_information(account_id)