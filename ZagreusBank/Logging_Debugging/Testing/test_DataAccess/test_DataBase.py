import ZagreusBank.Release.DataManagement.Database.PostgresAccessClasses.postgres_Account as Account_dao
import ZagreusBank.Release.DataManagement.Database.PostgresAccessClasses.postgres_Customer as Customer_dao


def test_create_account(self, new_account: DAL.Account) -> DAL.Account or str:
    try:
        account_creation_request = "insert into account values(default, %s, %s, false) returning account_id"
        sql_request_handler = db_connection.cursor()

        sql_request_handler.execute(account_creation_request, (new_account.balance, new_account.customer_id))
        db_connection.commit()

        account_id = sql_request_handler.fetchone()[0]
        new_account.account_id = account_id
        return new_account
    except (E.AccountCreationException, E.ForeignKeyViolation) as e:
        return str(e)


def test_update_account_information():
    test_value = Account_dao.postgres_Account.update_account_information()
    pass

def test_is_on_hold(self, account_id: int) -> bool:
    pass


def test_get_account_information():
    pass


def test_get_accounts_by_customer_id():
    pass


def test_close_account():
    pass