import ZagreusBank.Release.DataManagement.DataAccessClasses.dao_Customer as CustomerDataManipulation


class imp_Customer(CustomerDataManipulation.dao_Customer):
    def create_customer_entry(self, customer: CustomerDataManipulation.Customer) -> CustomerDataManipulation.Customer:
        print("fix me")

    def get_customer_information(self, customer_id: int) -> CustomerDataManipulation.Customer:
        print("fix me")

    def get_all_customer_information(self) -> list[CustomerDataManipulation.Customer]:
        print("fix me")

    def update_customer_information(self, customer: CustomerDataManipulation.Customer) -> CustomerDataManipulation.Customer:
        print("fix me")

    def delete_customer_information(self, customer_id: int) -> bool:
        print("fix me")

