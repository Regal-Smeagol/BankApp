from abc import abstractmethod, ABC
from BankApp.BankApp.Release.Util.AbstractClasses.dao_Account import dao_Account


class CustomerInterface(ABC, dao_Account):
    pass
