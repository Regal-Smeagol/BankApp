from abc import abstractmethod, ABC


class BankSystem(ABC):

    @abstractmethod
    def create_account(self, account_details: str):
        pass

    @abstractmethod
    def get_account_by_id(self, id_number: int):
        pass

    @abstractmethod
    def deposit(self, id_number: int, ):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def transfer(self):
        pass

    @abstractmethod
    def update_customer_info(self):
        pass

    @abstractmethod
    def retrieve_customer_info(self):
        pass

    @abstractmethod
    def close_account(self):
        pass

    @abstractmethod
    def customer_departure(self):
        pass

    @abstractmethod
    def transaction_validation(self):
        pass

    @abstractmethod
    def add_customer(self):
        pass

    @abstractmethod
    def retrieve_list_of_customers(self):
        pass

    @abstractmethod
    def retrieve_list_of_accounts(self):
        pass

    @abstractmethod
    def retrieve_list_of_accounts_by_cust_id(self):
        pass


"""
    class Customer():
        pass

    class Account():
        pass
        # account num
        # customer ID
        # Balance
        # On hold or not
        # limit
        # interest rate if any
        #
"""
