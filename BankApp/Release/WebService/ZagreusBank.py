from typing import Optional, Any

from flask import Flask, request, jsonify # Library used for running a microservice used for testing and debugging

from BankApp.Release.DataManagement.DataClasses.Customer import Customer

ZagreusBankServer: Flask = Flask(__name__)


@ZagreusBankServer.get("/")
def landing_page():
    return "Welcome to Jurassic Park"


# @ZagreusBankServer.post("/customer")
# def create_customer_record():
#     try:
#         customer_data = request.get_json()
#         new_customer = Customer(customer_data)
#     except DuplicateCustomerException as e:
#         return e


@ZagreusBankServer.get("/customer/<customer_id>")
def return_customer_information(customer_id: str):
    json_customer = jsonify(int(customer_id))
    return json_customer


ZagreusBankServer.run()
