from ZagreusBank.Version2.data_access_layer.abstract_classes.Customer_dao import CustomerDAO
from ZagreusBank.Version2.entities.Customer import Customer
from ZagreusBank.ZagreusDBConnection import database_connection_object


class CustomerPostgresDAO(CustomerDAO):
    def create_customer(self, customer: Customer) -> Customer:
        sql = "insert into customer values(default, %s, %s) returning customer_id"
        sql_request_handler = database_connection_object.cursor()
        sql_request_handler.execute(sql, (customer.first_name, customer.last_name))
        database_connection_object.commit()
        generated_id = sql_request_handler.fetchone()[0]
        customer.customer_id = generated_id
        return customer

    def get_customer_by_id(self, customer_id: int) -> Customer:
        get_customer_request = "select * from customer where customer_id = %s"
        sql_request_handler = database_connection_object.cursor()
        sql_request_handler.execute(get_customer_request, [customer_id])
        customer_record = sql_request_handler.fetchone()
        customer = Customer(*customer_record)
        return customer

    def get_all_customers(self) -> list[Customer]:
        get_all_customers_request = "select * from customer"
        sql_request_handler = database_connection_object.cursor()
        sql_request_handler.execute(get_all_customers_request)
        customer_records = sql_request_handler.fetchall()
        customers = []
        for customer in customer_records:
            customers.append(Customer(*customer))
        return customers

    def update_customer_information(self, customer: Customer) -> Customer:
        sql = "update customer set first_name = %s, last_name = %s where customer_id = %s"
        sql_request_handler = database_connection_object.cursor()
        sql_request_handler.execute(sql, (customer.first_name, customer.last_name, customer.customer_id))
        database_connection_object.commit()
        return customer

    def delete_customer_information(self, customer_id: int) -> bool:
        sql = "delete from customer where customer_id = %s"
        sql_request_handler = database_connection_object.cursor()
        sql_request_handler.execute(sql, [customer_id])
        database_connection_object.commit()
        return True
