"""Code for the server, HTTP requests, and parsing data, respectively"""
from flask import Flask, request, jsonify

"""Data Classes"""
from ZagreusBank.Release.DataManagement.DataClasses.Account import Account
from ZagreusBank.Release.DataManagement.DataClasses.Customer import Customer

"""Code for logging"""
import logging
logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

"""Code for bank management and logical operations"""
from ZagreusBank.Release.Service.BankSystem import BankSystem

"""Local Implementation Objects"""
#from ZagreusBank.Release.DataManagement.LocalImplementationClasses.imp_Customer import imp_Customer
#from ZagreusBank.Release.DataManagement.LocalImplementationClasses.imp_Account import imp_Account



"""Custom Exceptions"""
#from ZagreusBank.Logging_Debugging.CustomExceptions.DuplicateCustomerException import DuplicateCustomerException
#from ZagreusBank.Logging_Debugging.CustomExceptions.DuplicateAccountNumberException import DuplicateAccountNumberException

ZagreusWebServer: Flask = Flask(__name__)

BankSystem()


@ZagreusWebServer.get("/")
def landing_page():
    return "Welcome to Zagreus Bank"


@ZagreusWebServer.get("customer/all")
def return_all_customer_information():
    imp_Customer.get_all_customer_information()


@ZagreusWebServer.get("/customer/new")
def create_customer_record():
    try:
        customer_data = request.get_json()
        new_customer = Account(**customer_data)
        created_customer =
    except DuplicateCustomerException as e:
        json_exception_response = jsonify(dict(message=e))
        return json_exception_response


@ZagreusWebServer.get("/customer/<customer_id>")
def return_customer_information(customer_id: str):
    json_customer_info = jsonify(int(customer_id))
    return json_customer_info


@ZagreusWebServer.get("/account/<account_id>")
def return_account_information(account_id: str):
    json_account_info = jsonify((int(account_id)))
    return json_account_info


@ZagreusWebServer.post("account/new/<customer_id>")
def make_account_for_customer_id(customer_id: str):
    imp_Customer.get_customer_information(int(customer_id))

@ZagreusWebServer.post("transfer/<sending_account_id>/<receiving_account_id>")
def balance_transfer:


ZagreusWebServer.run()
