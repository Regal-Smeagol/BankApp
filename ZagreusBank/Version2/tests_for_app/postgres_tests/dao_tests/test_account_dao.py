from ZagreusBank.Version2.data_access_layer.implementation_classes.Account_postgres_dao import AccountPostgresDAO
from ZagreusBank.Version2.entities.Account import Account

account_dao = AccountPostgresDAO()
account: Account = Account(7, 5, 207.50, False)

random_account_data = [dict(account_id=1, customer_id=5, balance=100.25, on_hold=True),
                       dict(account_id=3, customer_id=3, balance=173.39, on_hold=True),
                       dict(account_id=4, customer_id=2, balance=9028.20, on_hold=True),
                       dict(account_id=6, customer_id=3, balance=87.72, on_hold=True)]

random_account: dict = random_account_data.pop()

update_account = Account(**random_account)

account_to_delete = Account(**(random_account_data.pop()))


def test_create_account_success():
    created_account = account_dao.create_account_entry(account)
    assert created_account.account_id != 0
    print(created_account)


def test_get_account_success():
    test_account: Account = account_dao.get_account_information(1)
    assert test_account.account_id != 0
    print(test_account)


def test_get_all_accounts_success():
    accounts = account_dao.get_all_accounts_information()
    assert len(accounts) > 2
    print(accounts)


def test_update_account_success():
    updated_account = account_dao.update_account_information(update_account)
    assert updated_account.account_id == random_account["account_id"]
    print(updated_account)


def test_delete_account_success():
    account_to_be_deleted = account_dao.create_account_entry(account_to_delete)
    result = account_dao.delete_account_information(account_to_be_deleted.account_id)
    assert result
