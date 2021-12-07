from BankApp.ZagreusBank.Version2.data_access_layer.implementation_classes.Account_dao_imp import AccountDAOImp
from BankApp.ZagreusBank.Version2.data_access_layer.implementation_classes.Account_postgres_dao import AccountPostgresDAO
from BankApp.ZagreusBank.Version2.entities.Account import Account

account_dao_imp = AccountDAOImp()
account = Account(1, 1, 0.0, False)


def test_create_account_success():
    new_account = account_dao_imp.create_account_entry(account)
    for accounts in account_dao_imp.account_list:
        print(accounts)
    print(new_account.account_id)
    assert new_account.account_id != 0


def test_get_account_success():
    returned_account: Account = account_dao_imp.get_account_information(1)
    assert returned_account.account_id == 1


def test_get_all_accounts_success():
    account_list = account_dao_imp.get_all_accounts_information()
    assert len(account_list) >= 2


def test_update_account_success():
    updated_info = Account(1, 1, 105, True)
    updated_account: Account = account_dao_imp.update_account_information(updated_info)
    assert updated_account.account_id == updated_info.account_id


def test_delete_account_success():
    confirm_account_deleted = account_dao_imp.delete_account_information(3)
    assert confirm_account_deleted
