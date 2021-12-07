from typing import List

import ZagreusBank.Release.DataManagement.Database.PostgresAccessClasses.postgres_Account as daoAccount

acc_dao_obj = daoAccount.postgres_Account(0, 1, 0.0, False)
test_account_one = {'account_id': 5, 'customer_id': 1, 'balance': 700, 'on_hold': True}


def test_create_account():
    test_account = acc_dao_obj.create_account(daoAccount.DataAccess.Account(**test_account_one))
    assert isinstance(test_account, daoAccount.DataAccess.Account)  # fails the test if an exception was caught
    assert test_account.account_id != 0
    print(test_account)


def test_update_account_information():
    test_account = daoAccount.DataAccess.Account(**test_account_one)
    test_value = acc_dao_obj.update_account_information(test_account)
    assert isinstance(test_value, daoAccount.DataAccess.Account)
    print(test_value.account_id)
    print(test_value.customer_id)
    print(test_value.balance)
    print(test_value.is_on_hold)
    assert test_value.account_id == test_account_one["account_id"] and test_value.customer_id == test_account_one["customer_id"] and test_value.balance == test_account_one["balance"] and test_value.is_on_hold == test_account_one["on_hold"]



def test_is_on_hold():
    test_bool = acc_dao_obj.is_on_hold(1)
    assert isinstance(test_bool, bool)  # fails is test an exception was returned


def test_get_account_information():
    test_account = acc_dao_obj.get_account_information(test_account_one[0])
    print('\n')
    print(test_account)
    assert isinstance(test_account, daoAccount.DataAccess.Account)


def test_get_accounts_by_customer_id():
    test_account = acc_dao_obj.get_accounts_by_customer_id(1)
    print('\n')
    print(test_account)
    assert isinstance(test_account, List)
    for account in test_account:
        print(str(account))


def test_close_account():
    pass
