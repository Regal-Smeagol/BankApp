class Account:
    """Class Variables"""
    total_active_accounts: int = 0
    accounts_on_record: int = 0

    def __init__(self, account_id: int, customer_id: int, balance: float, on_hold: bool):
        # default variables to be replaced
        self.account_id: int = account_id
        self.customer_id: int = customer_id
        self.balance: float = balance
        self.is_on_hold: bool = on_hold

    def __str__(self):
        return f"Account ID: {self.account_id}\nCustomer ID: {self.customer_id}\nBalance: {self.balance}\nHOLD: {self.is_on_hold}"

    def __dict__(self):
        return dict(account_id=self.account_id, customer_id=self.customer_id, balance=self.balance, is_on_hold=self.is_on_hold)

    """Class Utilities for Local Implementation"""

    @classmethod
    def increment_accounts_on_record(cls):
        cls.accounts_on_record += 1

    @classmethod
    def increment_active_accounts(cls):
        cls.total_active_accounts += 1

    @classmethod
    def decrement_accounts_on_record(cls):
        cls.accounts_on_record -= 1

    @classmethod
    def decrement_active_accounts(cls):
        cls.total_active_accounts -= 1

    @classmethod
    def account_id_generator(cls) -> int:
        return int(cls.accounts_on_record * 22 / 7)
