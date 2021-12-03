from ZagreusBank.Secrets.database_connection_config import config_dictionary
from psycopg import connect, OperationalError


def establish_connection():
    try:
        connection = connect(
            host=config_dictionary["host"],
            dbname=config_dictionary["dbname"],
            user=config_dictionary["user"],
            password=config_dictionary["password"],
            port=config_dictionary["port"]
        )
        return connection
    except OperationalError as e:
        print(str(e))


connection_obj = establish_connection()

print(connection_obj)
