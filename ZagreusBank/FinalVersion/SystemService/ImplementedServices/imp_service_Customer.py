import ZagreusBank.FinalVersion.Logging_Debugging.CustomExceptions as errors
from ZagreusBank.FinalVersion.SystemService.AbstractServices.abs_service_Customer import abs_service_Customer
from ZagreusBank.FinalVersion.DataManagement.DataClasses.Customer import Customer

from ZagreusBank.FinalVersion.DataManagement.PostgresDataAccessClasses.postgres_Customer import postgres_Customer as CustomerDAO


class imp_service_Customer(abs_service_Customer):
    def __init(self):
        self.customer_dao = CustomerDAO()

    def service_create_customer_entry(self, new_customer: Customer) -> Customer:
        created_customer = self.customer_dao.create_customer_entry(new_customer)
        return created_customer

    def service_update_customer_information(self, customer: Customer) -> Customer:
        updated_customer = self.customer_dao.update_customer_information(customer)
        return updated_customer

    def service_get_customer_information(self, customer_id: int) -> Customer:
        customer = self.customer_dao.get_customer_information(customer_id)
        return customer

    def service_get_all_customer_information(self) -> list[Customer]:
        all_customers = self.customer_dao.get_all_customer_information()
        return all_customers

    def service_delete_customer_information(self, customer_id: int) -> bool:
        return self.customer_dao.delete_customer_information(customer_id)


