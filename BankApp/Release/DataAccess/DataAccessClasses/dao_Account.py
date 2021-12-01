from abc import abstractmethod, ABC


class dao_Account(ABC):

    @abstractmethod
    def on_hold(self):
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
