import ZagreusBank.Release.DataManagement.Database.PostgresAccessClasses.postgres_Account as Account_dao
import ZagreusBank.Release.DataManagement.Database.PostgresAccessClasses.postgres_Customer as Customer_dao

default_account = Account_dao.DAL.Account(0, 1, 0.0, False)
acc_dao_obj = Account_dao.postgres_Account(default_account.account_id, default_account.customer_id,
                                           default_account.balance, default_account.is_on_hold)


def test_create_account():
    test_account = Account_dao.postgres_Account.create_account(acc_dao_obj, default_account)
    assert isinstance(test_account, Account_dao.DAL.Account) # fails the test if an exception was caught
    assert test_account.account_id != 0


def test_update_account_information():
    test_value = Account_dao.postgres_Account.update_account_information()
    pass


def test_is_on_hold():
    pass


def test_get_account_information():
    pass


def test_get_accounts_by_customer_id():
    pass


def test_close_account():
    pass
