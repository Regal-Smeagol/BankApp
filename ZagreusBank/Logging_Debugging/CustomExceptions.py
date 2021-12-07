from psycopg.errors import ForeignKeyViolation, InFailedSqlTransaction


class DuplicateAccountNumberException(Exception):
    def __init__(self, message: str):
        self.message = message


class DuplicateCustomerNumberException(Exception):
    def __init__(self, message: str):
        self.message = message


class AccountIsOnHoldException(Exception):
    def __init__(self, message: str):
        self.message = message


class RecordDoesNotExistException(Exception):
    def __init__(self, message: str):
        self.message = message


class AccountCreationException(Exception):
    def __init__(self, message: str):
        self.message = message


class AccountDoesNotExistException(Exception):
    def __init__(self, message: str):
        self.message = message


class UpdateAccountException(Exception):
    def __init__(self, message: str):
        self.message = message
