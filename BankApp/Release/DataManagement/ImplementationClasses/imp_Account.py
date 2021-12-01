from BankApp.Release.DataManagement.DataAccessClasses.dao_Account import dao_Account


def account_constructor(account_data):
    account = dao_Account.Account().__init__(account_data)
