from abc import abstractmethod, ABC
from ZagreusBank.Release.DataManagement.DataClasses.Customer import Customer


class abs_service_Customer(ABC):

    @abstractmethod
    def service_create_customer_entry(self, new_customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_get_customer_information(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def service_get_all_customer_information(self) -> list[Customer]:
        pass

    @abstractmethod
    def service_update_customer_information(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_delete_customer_information(self, customer_id: int) -> bool:
        pass
