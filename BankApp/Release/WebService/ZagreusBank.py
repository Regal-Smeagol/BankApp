"""Zagreus Bank: Gold is old! Crypto is hip, bro!!!"""
from flask import Flask, request, jsonify  # Code for the server, HTTP requests, and parsing data, respectively


"""Code for bank management and logical operations"""
from BankApp.Release.Service.BankSystem import BankSystem

"""Implementation Namespaces"""
import BankApp.Release.DataManagement.ImplementationClasses.imp_Customer
import BankApp.Release.DataManagement.ImplementationClasses.imp_Account


"""Custom Exceptions"""
from BankApp.Logging_Debugging.CustomExceptions.DuplicateCustomerException import DuplicateCustomerException
from BankApp.Logging_Debugging.CustomExceptions.DuplicateAccountNumberException import DuplicateAccountNumberException

ZagreusBankServer: Flask = Flask(__name__)

BankSystem()


@ZagreusBankServer.get("/")
def landing_page():
    return "Welcome to Jurassic Park"


@ZagreusBankServer.post("/new_customer")
def create_customer_record():
    try:
        customer_data = request.get_json()
        new_customer = imp_Customer.imp_Customer.create_customer_entry()
    except DuplicateCustomerException as e:
        json_exception_response = jsonify(dict(message=e))
        return json_exception_response


@ZagreusBankServer.get("/customer/<customer_id>")
def return_customer_information(customer_id: str):
    json_customer_info = jsonify(int(customer_id))
    return json_customer_info


ZagreusBankServer.run()
