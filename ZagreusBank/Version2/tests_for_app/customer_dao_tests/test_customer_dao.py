from BankApp.ZagreusBank.Version2.data_access_layer.implementation_classes.Customer_dao_imp import CustomerDAOImp
from BankApp.ZagreusBank.Version2.entities.Customer import Customer

customer_dao = CustomerDAOImp()
test_customer = Customer(0, "Test", "Customer")
updated_customer = Customer(0, "updated", "customer")


def test_create_customer_success():
    created_customer: Customer = customer_dao.create_customer(test_customer)
    assert created_customer.customer_id != 0


def test_select_customer_by_id_success():
    selected_customer: Customer = customer_dao.get_customer_by_id(1)
    assert selected_customer.customer_id == 1


def test_select_all_customers_success():
    customers: list[Customer] = customer_dao.get_all_customers()
    assert len(customers) >= 2


def test_update_customer_success():
    result: Customer = customer_dao.update_customer_information(updated_customer)
    assert result.first_name == updated_customer.first_name and result.last_name == updated_customer.last_name


def test_delete_customer_success():
    result: bool = customer_dao.delete_customer_information(0)
    assert result
