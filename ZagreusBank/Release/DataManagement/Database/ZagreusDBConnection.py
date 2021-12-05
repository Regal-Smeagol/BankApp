from ZagreusBank.Secrets.database_connection_config import credentials
from psycopg import connect, OperationalError


def establish_connection():
    try:
        connection = connect(
            host=credentials["host"],
            dbname=credentials["dbname"],
            user=credentials["user"],
            password=credentials["password"],
            port=credentials["port"]
        )
        return connection
    except OperationalError as e:
        print(str(e))


database_connection_object = establish_connection()

print(database_connection_object)
