from abc import abstractmethod, ABC
from ZagreusBank.Release.DataManagement.DataClasses.Customer import Customer


class dao_Customer(ABC, Customer):
    # create customer method
    @abstractmethod
    def create_customer_entry(self, customer: Customer) -> Customer:
        pass

    # get customer information
    @abstractmethod
    def get_customer_information(self, customer_id: int) -> Customer:
        pass

    # get all customer information
    @abstractmethod
    def get_all_customer_information(self) -> list[Customer]:
        pass

    # update customer information
    @abstractmethod
    def update_customer_information(self, customer: Customer) -> Customer:
        pass

    # delete customer information
    @abstractmethod
    def delete_customer_information(self, customer_id: int) -> bool:
        pass
