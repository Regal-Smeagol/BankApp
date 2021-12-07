from ZagreusBank.Version2.data_access_layer.abstract_classes.Account_dao import AccountDAO
from ZagreusBank.Version2.entities.Account import Account


class AccountDAOImp(AccountDAO):
    # these accounts are premade so that we can test our methods
    premade_account = Account(0, 1, 100, False)
    premade_account_two = Account(1, 1, 101, True)
    to_delete = Account(2, 1, 0, False)

    # we are going to use this list as our "database"
    account_list = [premade_account, premade_account_two, to_delete]
    # we are going to use this value to assign unique account ids
    account_id_generator = 4

    def create_account_entry(self, account: Account) -> Account:
        account.account_id = AccountDAOImp.account_id_generator
        AccountDAOImp.account_id_generator += 1
        AccountDAOImp.account_list.append(account)
        return account

    def get_account_information(self, account_id: int) -> Account:
        for account in AccountDAOImp.account_list:
            if account.account_id == account_id:
                return account

    def get_all_accounts_information(self) -> list[Account]:
        return AccountDAOImp.account_list

    def update_account_information(self, account: Account) -> Account:
        for account_in_list in AccountDAOImp.account_list:
            if account_in_list.account_id == account.account_id:
                index = AccountDAOImp.account_list.index(account_in_list)
                AccountDAOImp.account_list[index] = account
                return account

    def delete_account_information(self, account_id: int) -> bool:
        for account_in_list in AccountDAOImp.account_list:
            if account_in_list.account_id == account_id:
                index = AccountDAOImp.account_list.index(account_in_list)
                del AccountDAOImp.account_list[index]
                return True
