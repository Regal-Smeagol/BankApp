from abc import abstractmethod, ABC
from BankApp.Release.DataManagement.DataClasses.Account import Account


class dao_Account(ABC, Account):

    @abstractmethod
    def on_hold(self) -> bool:
        pass

    @abstractmethod
    def deposit(self, id_number: int, ):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def close_account(self):
        pass
