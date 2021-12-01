from flask import Flask, request, jsonify # Library used for running a microservice used for testing and debugging

from BankApp.BankApp.Release.DataAccess.DataClasses.Customer import Customer

ZagreusBankServer: Flask = Flask(__name__)


@ZagreusBankServer.get("/")
def landing_page():
    return "Welcome to Jurassic Park"


@ZagreusBankServer.post("/customer")
def create_customer_record():
    try:
        customer_data = request.get_json()
        new_customer = Customer(
            customer_data["first_name"],
            customer_data["last_name"],
            customer_data["customer_id"]
        )
    except ModuleNotFoundError as e:
        return e


@ZagreusBankServer.get("/customer/<customer_id>")
def return_customer_information(customer_id: str):
    json_customer = jsonify(int(customer_id))
    return json_customer


ZagreusBankServer.run()
