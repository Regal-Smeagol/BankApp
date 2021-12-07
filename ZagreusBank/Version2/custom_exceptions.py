class DuplicateAccountNumberException(Exception):
    def __init__(self, message: str):
        self.message = message


class DuplicateCustomerRecordException(Exception):
    def __init__(self, message: str):
        self.message = message
