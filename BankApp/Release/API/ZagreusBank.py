from flask import Flask, request, jsonify

ZagreusBankServer: Flask = Flask(__name__)


@ZagreusBankServer.get("/")
def landing_page():
    return "Homepage"


ZagreusBankServer.run()
