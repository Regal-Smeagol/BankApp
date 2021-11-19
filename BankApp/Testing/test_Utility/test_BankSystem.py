from BankApp.Release.Utility.Interfaces.BankSystemInterface import BankSystem


class Bank_Sys_Obj(BankSystem):

    def __init__(self):
        pass

    def create_account(self, account_details: str):
        pass

    def get_account_by_id(self, id_number: int):
        pass

    def deposit(self, id_number: int):
        pass

    def withdraw(self):
        pass

    def transfer(self):
        pass

    def update_customer_info(self):
        pass

    def retrieve_customer_info(self):
        pass

    def close_account(self):
        pass

    def customer_departure(self):
        pass

    def transaction_validation(self):
        pass

    def add_customer(self):
        pass

    def retrieve_list_of_customers(self):
        pass

    def retrieve_list_of_accounts(self):
        pass

    def retrieve_list_of_accounts_by_customer_id(self):
        pass


bank_obj = Bank_Sys_Obj()


def test_bank():
    assert type(bank_obj) is type(bank_obj)


def test_default_tester():
    print('\n\t* I can do anything with pytest')
    assert True
