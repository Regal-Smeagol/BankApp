from ZagreusBank.FinalVersion.DataManagement.DataClasses.Customer import Customer
from ZagreusBank.FinalVersion.DataManagement.AbstractDataAccessClasses.dao_Customer import dao_Customer

from ZagreusBank.ZagreusDBConnection import database_connection_object as db_connection


class postgres_Customer(dao_Customer):

    def create_customer_entry(self, new_customer: Customer) -> Customer:
        customer_creation_request = "insert into customer values(default, %s, %s) returning customer_id"
        sql_request_handler = db_connection.cursor()
        sql_request_handler.execute(customer_creation_request, (new_customer.first_name, new_customer.last_name))
        db_connection.commit()
        customer_id = sql_request_handler.fetchone()[0]
        new_customer.customer_id = customer_id
        return new_customer

    def get_customer_information(self, customer_id: int) -> Customer:
        get_customer_information_request = "select * from customer where customer_id = %s"
        sql_request_handler = db_connection.cursor()
        sql_request_handler.execute(get_customer_information_request, [customer_id])
        customer_data = sql_request_handler.fetchone()
        customer = Customer(*customer_data)
        sql_request_handler.close()
        return customer

    def get_all_customer_information(self) -> list[Customer]:
        pass

    def update_customer_information(self, customer: Customer) -> Customer:
        update_customer_request = "update customer set first_name = %s, last_name = %s where customer_id = %s"
        sql_request_handler = db_connection.cursor()
        sql_request_handler.execute(update_customer_request,
                                    (customer.first_name, customer.last_name, customer.customer_id))
        db_connection.commit()
        updated_account = postgres_Customer.get_customer_information(customer.customer_id)
        return updated_account

    def delete_customer_information(self, customer_id: int) -> bool:
        pass
