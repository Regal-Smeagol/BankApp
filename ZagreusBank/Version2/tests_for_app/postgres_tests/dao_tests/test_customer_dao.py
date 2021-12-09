from ZagreusBank.Version2.data_access_layer.implementation_classes.Customer_postgres_dao import CustomerPostgresDAO
from ZagreusBank.Version2.entities.Customer import Customer

customer_dao = CustomerPostgresDAO()

new_customer = Customer(0, "Test",  "Customer")
customer_names = [
                dict(first_name="Bryan", last_name="Brown"),
                dict(first_name="Son", last_name="Goku"),
                dict(first_name="Manny", last_name="MacCloud"),
                dict(first_name="Amy", last_name="Brown")
                ]
new_name = customer_names.pop()
update_customer = Customer(3, **new_name)

deleted_name = customer_names.pop()
delete_customer = Customer(100, **deleted_name)


def test_create_customer_success():
    customer_result = customer_dao.create_customer(new_customer)
    assert customer_result.customer_id != 0
    print(customer_result)


def test_select_customer_by_id_success():
    initial_customer = customer_dao.get_customer_by_id(1)
    assert initial_customer.customer_id == 1
    print(initial_customer)


def test_select_all_customers_success():
    customers = customer_dao.get_all_customers()
    assert len(customers) >= 3
    for customer in customers:
        print(customer)


def test_update_customer_success():
    updated_customer = customer_dao.update_customer_information(update_customer)
    assert updated_customer.first_name == new_name["first_name"] and updated_customer.last_name == new_name["last_name"]
    print(updated_customer)


def test_delete_customer_success():
    to_be_deleted = customer_dao.create_customer(delete_customer)
    result = customer_dao.delete_customer_information(to_be_deleted.customer_id)
    assert result
    print(to_be_deleted)
    print(result)
