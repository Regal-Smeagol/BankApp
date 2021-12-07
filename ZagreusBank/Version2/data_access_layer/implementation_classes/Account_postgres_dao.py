from ZagreusBank.Version2.data_access_layer.abstract_classes.Account_dao import AccountDAO

from ZagreusBank.ZagreusDBConnection import database_connection_object

from ZagreusBank.Version2.entities.Account import Account


class AccountPostgresDAO(AccountDAO):
    def create_account_entry(self, account: Account) -> Account:
        create_account_request = "insert into account values(default, %s, %s, %s) returning account_id"
        sql_request_handler = database_connection_object.cursor()
        sql_request_handler.execute(create_account_request, (account.customer_id, account.balance, account.is_on_hold))
        database_connection_object.commit()
        account_id = sql_request_handler.fetchone()[0]
        account.account_id = account_id
        return account

    def get_account_information(self, account_id: int) -> Account:
        get_account_request = "select * from account where account_id = %s"
        sql_request_handler = database_connection_object.cursor()
        sql_request_handler.execute(get_account_request, [account_id])
        account_record = sql_request_handler.fetchone()
        account = Account(*account_record)
        return account

    def get_all_accounts_information(self) -> list[Account]:
        get_all_accounts_request = "select * from account"
        sql_request_handler = database_connection_object.cursor()
        sql_request_handler.execute(get_all_accounts_request)
        account_records = sql_request_handler.fetchall()
        account_list = []
        for account in account_records:
            account_list.append(Account(*account))
        return account_list

    def update_account_information(self, account: Account) -> Account:
        update_account_request = "update account set customer_id = %s, balance = %s, on_hold = %s where account_id = %s"
        sql_request_handler = database_connection_object.cursor()
        sql_request_handler.execute(update_account_request, (account.customer_id, account.balance, account.is_on_hold, account.account_id))
        database_connection_object.commit()
        return account

    def delete_account_information(self, account_id: int) -> bool:
        sql = "delete from account where account_id = %s"
        sql_request_handler = database_connection_object.cursor()
        sql_request_handler.execute(sql, [account_id])
        database_connection_object.commit()
        return True
