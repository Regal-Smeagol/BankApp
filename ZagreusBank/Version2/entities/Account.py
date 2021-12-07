class Account:
    def __init__(self, account_id: int, customer_id: int, balance: float, on_hold: bool):
        # default variables to be replaced
        self.account_id: int = account_id
        self.customer_id: int = customer_id
        self.balance: float = balance
        self.is_on_hold: bool = on_hold

    def __str__(self):
        return f"Account ID: {self.account_id}\nCustomer ID: {self.customer_id}\nBalance: {self.balance}\nHOLD: {self.is_on_hold}"

    def make_account_dictionary(self):
        return dict(account_id=self.account_id, customer_id=self.customer_id, balance=self.balance, is_on_hold=self.is_on_hold)
