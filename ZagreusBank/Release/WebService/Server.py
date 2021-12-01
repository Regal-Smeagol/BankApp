"""Zagreus Bank: Gold is old! Crypto is hip, bro!!!"""
from flask import Flask, request, jsonify  # Code for the server, HTTP requests, and parsing data, respectively

"""Code for bank management and logical operations"""
from ZagreusBank.Release.Service.BankSystem import BankSystem

"""Implementation"""
from ZagreusBank.Release.DataManagement.ImplementationClasses.imp_Customer import imp_Customer
from ZagreusBank.Release.DataManagement.ImplementationClasses.imp_Account import imp_Account

"""Custom Exceptions"""
from ZagreusBank.Logging_Debugging.CustomExceptions.DuplicateCustomerException import DuplicateCustomerException
from ZagreusBank.Logging_Debugging.CustomExceptions.DuplicateAccountNumberException import DuplicateAccountNumberException

ZagreusWebServer: Flask = Flask(__name__)

BankSystem()


@ZagreusWebServer.get("/")
def landing_page():
    return "Welcome to Zagreus Bank"


@ZagreusWebServer.get("/customer/new")
def create_customer_record():
    try:
        customer_data = request.get_json()
        new_customer = imp_Customer.create_customer_entry(customer_data)
    except DuplicateCustomerException as e:
        json_exception_response = jsonify(dict(message=e))
        return json_exception_response


@ZagreusWebServer.get("/customer/<customer_id>")
def return_customer_information(customer_id: str):
    json_customer_info = jsonify(int(customer_id))
    return json_customer_info


ZagreusWebServer.run()
