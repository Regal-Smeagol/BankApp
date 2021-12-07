from ZagreusBank.Version2.data_access_layer.abstract_classes.Customer_dao import CustomerDAO
from ZagreusBank.Version2.entities.Customer import Customer


class CustomerDAOImp(CustomerDAO):

    # NEED TO ADD PREMADE DATA FOR TESTS WHEN THEY ARE CREATED
    customer_one = Customer(0, "first", "customer")
    customer_two = Customer(1, "second", "customer")
    customer_three = Customer(2, "to be", "deleted")
    customer_four = Customer(3, "duplicate", "name")
    customer_list = [customer_one, customer_two, customer_three, customer_four]
    customer_id_generator = 5

    def create_customer(self, customer: Customer) -> Customer:
        new_customer = customer
        new_customer.customer_id = CustomerDAOImp.customer_id_generator
        CustomerDAOImp.customer_id_generator += 1
        CustomerDAOImp.customer_list.append(new_customer)
        return new_customer

    def get_customer_by_id(self, customer_id: int) -> Customer:
        for customer in CustomerDAOImp.customer_list:
            if customer.customer_id == customer_id:
                return customer

    def get_all_customers(self) -> list[Customer]:
        return CustomerDAOImp.customer_list

    def update_customer_information(self, customer: Customer) -> Customer:
        for customer_in_list in CustomerDAOImp.customer_list:
            if customer_in_list.customer_id == customer.customer_id:
                customer_in_list.first_name = customer.first_name
                customer_in_list.last_name = customer.last_name
                return customer_in_list

    def delete_customer_information(self, customer_id: int) -> bool:
        for customer in CustomerDAOImp.customer_list:
            if customer.customer_id == customer_id:
                index = CustomerDAOImp.customer_list.index(customer)
                del CustomerDAOImp.customer_list[index]
                return True