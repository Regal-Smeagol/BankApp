import ZagreusBank.Version2.custom_exceptions as errors
from ZagreusBank.Version2.data_access_layer.implementation_classes.Customer_postgres_dao import CustomerPostgresDAO
from ZagreusBank.Version2.entities.Customer import Customer
from ZagreusBank.Version2.service_layer.abstract_services.Customer_service import CustomerService


class CustomerServiceImp(CustomerService):
    # business logic: must not have duplicate customer records

    def __init__(self, customer_dao: CustomerPostgresDAO):
        self.customer_dao = customer_dao

    def service_create_customer(self, customer: Customer) -> Customer:
        for existing_customer in self.customer_dao.customer_list:
            if existing_customer.first_name == customer.first_name and existing_customer.last_name == customer.last_name:
                raise errors.DuplicateCustomerRecordException("Error: Customer record already exists")
        new_customer = self.customer_dao.create_customer(customer)
        return new_customer

    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        return self.customer_dao.get_customer_by_id(customer_id)

    def service_get_all_customers(self) -> list[Customer]:
        return self.customer_dao.get_all_customers()

    def service_update_customer_information(self, customer: Customer) -> Customer:
        for existing_customer in self.customer_dao.customer_list:
            if existing_customer.customer_id != customer.customer_id:
                if existing_customer.first_name == customer.first_name and existing_customer.last_name == customer.last_name:
                    raise errors.DuplicateCustomerRecordException("Error: Customer record already exists")
        updated_customer = self.customer_dao.update_customer_information(customer)
        return updated_customer

    def service_delete_customer_information(self, customer_id: int) -> bool:
        return self.customer_dao.delete_customer_information(customer_id)
