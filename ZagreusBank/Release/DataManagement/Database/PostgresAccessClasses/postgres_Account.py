from typing import List

import ZagreusBank.Logging_Debugging.CustomExceptions.CustomeExceptions as E

import ZagreusBank.Release.DataManagement.DataAccessClasses.dao_Account as DAL
from ZagreusBank.Release.DataManagement.Database.ZagreusDBConnection import database_connection_object as db_connection


class postgres_Account(DAL.dao_Account):

    def create_account(self, new_account: DAL.Account) -> DAL.Account or str:
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

    def update_account_information(self, account_to_update: DAL.Account) -> DAL.Account:
        update_account_request = "update account set balance = %s, customer_id = %s, on_hold = %s where account_id = %s"
        sql_request_handler = db_connection.cursor()
        sql_request_handler.execute(update_account_request, (
            account_to_update.balance, account_to_update.customer_id, account_to_update.is_on_hold))
        db_connection.commit()
        updated_account = DAL.Account(*sql_request_handler.fetchone())
        return updated_account

    def is_on_hold(self, account_id: int) -> bool:
        on_hold_request = "select * from hold where account_id = %s returning on_hold"
        sql_request_handler = db_connection.cursor()
        sql_request_handler.execute(on_hold_request, account_id)
        db_connection.commit()
        hold = sql_request_handler.fetchone()[0]
        return hold

    def get_account_information(self, account_id: int) -> DAL.Account:
        account_information_request = "select * from account where account_id = %s"
        sql_request_handler = db_connection.cursor()
        sql_request_handler.execute(account_information_request, account_id)
        account_data = sql_request_handler.fetchone()
        account = DAL.Account(*account_data)
        return account

    def get_accounts_by_customer_id(self, customer_id: int) -> List[DAL.Account]:
        get_all_accounts_request = "select * from account where customer_id = %s"
        sql_request_handler = db_connection.cursor()
        sql_request_handler.execute(get_all_accounts_request, [customer_id])
        db_connection.execute()
        account_data = sql_request_handler.fetchall()
        accounts = []
        for account in account_data:
            accounts.append(DAL.Account(*account_data))
        return accounts

    def close_account(self, account_id: int) -> bool:
        try:
            success = True
            close_account_request = "delete from account where account_id = %s"
            sql_request_handler = db_connection.cursor()
            sql_request_handler.execute(close_account_request, [account_id])
            db_connection.commit()
            return success
        except (E.AccountDoesNotExistException, E.InFailedSqlTransaction) as e:
            return str(e)
