class Account:
    """Class Variables"""
    total_active_accounts: int = 0
    accounts_on_record: int = 0

    def __init__(self, account_data):
        self.account_id: int = self.account_id_generator()
        self.balance: float = 0.00

    def __str__(self):
        return f"Account ID: {self.account_id}, "

    """Class Utilities"""

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
