from abc import abstractmethod, ABC


class AccountInterface(ABC):
    # data
    account_number: int
    available_balance: float
    customer_id: int
    withdraw_limit: float
    interest_rate: float
    on_hold: bool # Used for storing whether or not a customer can access their account.


    @abstractmethod
    def on_hold(self):
        pass
