from abc import ABC, abstractmethod

from ZagreusBank.Version2.entities.Customer import Customer


class CustomerService(ABC):

    # create customer
    @abstractmethod
    def service_create_customer(self, customer: Customer) -> Customer:
        pass

    # get customer
    @abstractmethod
    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    # get all customers
    @abstractmethod
    def service_get_all_customers(self) -> list[Customer]:
        pass

    # update customer
    @abstractmethod
    def service_update_customer_information(self, customer: Customer) -> Customer:
        pass

    # delete customer
    @abstractmethod
    def service_delete_customer_information(self, customer_id: int) -> bool:
        pass
