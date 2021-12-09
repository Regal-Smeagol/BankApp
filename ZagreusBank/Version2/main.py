"""this is where my API will go: I will create a flask object here and define my routes and their functions here"""
from flask import Flask, request, jsonify

import custom_exceptions as errors

from ZagreusBank.Version2.data_access_layer.implementation_classes.Account_postgres_dao import AccountPostgresDAO
from ZagreusBank.Version2.data_access_layer.implementation_classes.Customer_postgres_dao import CustomerPostgresDAO
from ZagreusBank.Version2.entities.Account import Account
from ZagreusBank.Version2.entities.Customer import Customer
from ZagreusBank.Version2.service_layer.implementation_services.Account_postgres_service import AccountPostgresService
from ZagreusBank.Version2.service_layer.implementation_services.Customer_service_imp import CustomerServiceImp
import logging

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")


zagreus_bank_server: Flask = Flask(__name__)

account_dao = AccountPostgresDAO()
account_service = AccountPostgresService(account_dao)
customer_dao = CustomerPostgresDAO()
customer_service = CustomerServiceImp(customer_dao)


# create account method
@zagreus_bank_server.post("/account/new")
def create_account_entry():
    try:
        account_data = request.get_json()
        new_account = Account(
            0,
            account_data["customerID"],
            account_data["balance"],
            account_data["onHold"]
        )
        account_to_return = account_service.service_create_account_entry(new_account)
        account_as_dictionary = account_to_return.make_account_dictionary()
        account_as_json = jsonify(account_as_dictionary)
        return account_as_json
    except errors.DuplicateAccountNumberException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


# get account information
@zagreus_bank_server.get("/account/<account_id>")
def get_account_information(account_id: str):
    result = account_service.service_get_account_information(int(account_id))
    result_as_dictionary = result.make_account_dictionary()
    result_as_json = jsonify(result_as_dictionary)
    return result_as_json


# get all accounts information
@zagreus_bank_server.get("/account/all")
def get_all_accounts_information():
    accounts_as_accounts = account_service.service_get_all_accounts_information()
    accounts_as_dictionary = []
    for accounts in accounts_as_accounts:
        dictionary_account = accounts.make_account_dictionary()
        accounts_as_dictionary.append(dictionary_account)
    return jsonify(accounts_as_dictionary)


@zagreus_bank_server.patch("/account/<account_id>")
def update_account_information(account_id: str):
    try:
        account_data = request.get_json()
        new_account = Account(
            int(account_id),
            account_data["customer_id"],
            account_data["balance"],
            account_data["on_hold"]
        )
        updated_account = account_service.service_update_account_information(new_account)
        return "Account updated successfully, the account info is now " + str(updated_account)
    except errors.DuplicateAccountNumberException as e:
        return str(e)


# delete account information
@zagreus_bank_server.delete("/account/delete/<account_id>")
def delete_account_information(account_id: str):
    result = account_service.service_delete_account_information(int(account_id))
    if result:
        return "Account with id {} was deleted successfully".format(account_id)
    else:
        return "Something went wrong: account with id {} was not deleted".format(account_id)


@zagreus_bank_server.post("/customer")
def create_customer():
    try:
        body = request.get_json()
        new_customer = Customer(
            body["customer_id"],
            body["first_name"],
            body["last_name"]
        )
        created_customer = customer_service.service_create_customer(new_customer)
        created_customer_as_dictionary = created_customer.create_customer_dictionary()
        return jsonify(created_customer_as_dictionary), 201
    except errors.DuplicateCustomerRecordException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message), 400


@zagreus_bank_server.get("/customer/<customer_id>")
def get_customer_by_id(customer_id: str):
    customer = customer_service.service_get_customer_by_id(int(customer_id))
    customer_as_dictionary = customer.create_customer_dictionary()
    return jsonify(customer_as_dictionary), 200


@zagreus_bank_server.get("/customer/all")
def get_all_customers():
    customers = customer_service.service_get_all_customers()
    customers_as_dictionaries = []
    for customer in customers:
        dictionary_customer = customer.create_customer_dictionary()
        customers_as_dictionaries.append(dictionary_customer)
    return jsonify(customers_as_dictionaries), 200




@zagreus_bank_server.delete("/customer/delete/<customer_id>")
def delete_customer(customer_id: str):
    result = customer_service.service_delete_customer_information(int(customer_id))
    if result:
        return "Customer with id {} was deleted successfully".format(customer_id)
    else:
        return "Something went wrong: Customer with id {} was not deleted".format(customer_id)

#@zagreus_bank_server.post("transfer/<sending_account_id>/<receiving_account_id>/<amount>")
#def balance_transfer(sending_account_id: str, receiving_account_id: str, amount: str):




zagreus_bank_server.run()
