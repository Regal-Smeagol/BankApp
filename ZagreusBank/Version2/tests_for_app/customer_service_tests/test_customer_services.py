import BankApp.ZagreusBank.Version2.custom_exceptions as errors
from BankApp.ZagreusBank.Version2.data_access_layer.implementation_classes.Customer_dao_imp import CustomerDAOImp
from BankApp.ZagreusBank.Version2.entities.Customer import Customer
from BankApp.ZagreusBank.Version2.service_layer.implementation_services.Customer_service_imp import CustomerServiceImp

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)

bad_customer = Customer(0, "duplicate name")
bad_update_customer = Customer(1, "duplicate name")


def test_catch_creating_customer_with_duplicate_name():
    try:
        customer_service.service_create_customer(bad_customer)
        assert False
    except errors.DuplicateCustomerRecordException as e:
        assert str(e) == "Error: Customer record already exists"


def test_catch_updating_customer_with_duplicate_name():
    try:
        customer_service.service_update_customer_information(bad_update_customer)
        assert False
    except errors.DuplicateCustomerRecordException as e:
        assert str(e) == "Error: Customer record already exists"
