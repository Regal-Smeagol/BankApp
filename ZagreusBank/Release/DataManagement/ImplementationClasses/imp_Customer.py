from ZagreusBank.Release.DataManagement.DataAccessClasses.dao_Customer import dao_Customer
from ZagreusBank.Release.DataManagement.DataClasses.Customer import Customer


class imp_Customer(dao_Customer):
    def create_customer_entry(self, customer: Customer) -> Customer:
        print("fix me")

    def get_customer_information(self, customer_id: int) -> Customer:
        print("fix me")

    def get_all_customer_information(self) -> list[Customer]:
        print("fix me")

    def update_customer_information(self, customer: Customer) -> Customer:
        print("fix me")

    def delete_customer_information(self, customer_id: int) -> bool:
        print("fix me")

