from ZagreusBank.Release.DataManagement.DataAccessClasses.dao_Account import dao_Account
from ZagreusBank.Release.DataManagement.DataClasses.Account import Account

from ZagreusBank.ZagreusDBConnection import database_connection_object as db_connection


class postgres_Account(dao_Account):

    def create_account(self, new_account: Account) -> Account:
        account_creation_request = "insert into account values(default, %s, %s, false) returning account_id"
        sql_request_handler = db_connection.cursor()
        sql_request_handler.execute(account_creation_request, (new_account.customer_id, new_account.balance))
        db_connection.commit()
        account_id = sql_request_handler.fetchone()[0]
        new_account.account_id = account_id
        return new_account

    def update_account_information(self, account_to_update: Account) -> Account:
        update_account_request = "update account set balance = %s, customer_id = %s, on_hold = %s where account_id = %s"
        sql_request_handler = db_connection.cursor()
        sql_request_handler.execute(update_account_request, (account_to_update.balance, account_to_update.customer_id, account_to_update.is_on_hold, account_to_update.account_id))
        db_connection.commit()
        updated_account = postgres_Account.get_account_information(account_to_update.account_id)
        return updated_account

    def get_account_information(self, account_id: int) -> Account:
        account_information_request = "select * from account where account_id = %s"
        sql_request_handler = db_connection.cursor()
        sql_request_handler.execute(account_information_request, [account_id])
        account_data = sql_request_handler.fetchone()
        account = Account(*account_data)
        sql_request_handler.close()
        return account

    def is_on_hold(self, account_id: int) -> bool:
        hold_check = postgres_Account.get_account_information(account_id)
        return hold_check.is_on_hold

    def get_accounts_by_customer_id(self, customer_id: int) -> list[Account]:
        get_all_accounts_request = "select * from account where customer_id = %s"
        sql_request_handler = db_connection.cursor()
        sql_request_handler.execute(get_all_accounts_request, [customer_id])
        db_connection.commit()
        account_data = sql_request_handler.fetchall()
        accounts = []
        for account in account_data:
            accounts.append(Account(*account))
        sql_request_handler.close()
        return accounts

    def close_account(self, account_id: int) -> bool:
        try:
            success = True
            close_account_request = "delete from account where account_id = %s"
            sql_request_handler = db_connection.cursor()
            sql_request_handler.execute(close_account_request, [account_id])
            db_connection.commit()
            sql_request_handler.close()
            return success
        except Exception as e:
            return str(e)
