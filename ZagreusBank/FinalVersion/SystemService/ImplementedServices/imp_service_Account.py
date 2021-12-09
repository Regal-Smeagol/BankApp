import ZagreusBank.FinalVersion.Logging_Debugging.CustomExceptions as errors
from ZagreusBank.FinalVersion.SystemService.AbstractServices.abs_service_Account import abs_service_Account
from ZagreusBank.FinalVersion.DataManagement.DataClasses.Account import Account

from ZagreusBank.FinalVersion.DataManagement.PostgresDataAccessClasses.postgres_Account import postgres_Account as AccountDAO


class imp_service_Account(abs_service_Account):
    def __init(self):
        self.account_dao = AccountDAO()

    def service_create_account(self, new_account: Account) -> Account:
        created_account = self.account_dao.create_account(new_account)
        return created_account

    def service_update_account_information(self, account: Account) -> Account:
        updated_account = self.account_dao.update_account_information(account)
        return updated_account

    def service_get_account_information(self, account_id: int) -> Account:
        account = self.account_dao.get_account_information(account_id)
        return account

    def service_get_all_account_information(self) -> list[Account]:
        all_accounts = self.account_dao.get_all_account_information()
        return all_accounts

    def service_get_accounts_by_customer_id(self, customer_id: int) -> list[Account]:
        all_accounts_for_customer = self.account_dao.get_accounts_by_customer_id(customer_id)
        return all_accounts_for_customer

    def service_close_account(self, account_id: int) -> bool:
        return self.account_dao.close_account(account_id)


