import BankApp.ZagreusBank.Version2.custom_exceptions as errors
from BankApp.ZagreusBank.Version2.data_access_layer.implementation_classes.Account_dao_imp import AccountDAOImp
from BankApp.ZagreusBank.Version2.entities.Account import Account
from BankApp.ZagreusBank.Version2.service_layer.implementation_services.Account_service_imp import AccountServiceImp

account_dao = AccountDAOImp()
account_service = AccountServiceImp(account_dao)
account = Account(1, 1, 100, False)
account_update = Account(1, 1, 200, True)


def test_validate_create_account_method():
    try:
        for existing_account in account_service.account_dao.account_list:
            print(existing_account)
        unexpected_account = account_service.service_create_account_entry(account)
        print()
        for existing_account in account_service.account_dao.account_list:
            print(existing_account)
            print()
        print(unexpected_account.account_id)
        assert False
    except errors.DuplicateAccountNumberException as e:
        assert str(e) == "Account already exists"


def test_validate_update_account_method():
    try:
        account_service.service_update_account_information(account_update)
        assert False
    except errors.DuplicateAccountNumberException as e:
        assert str(e) == "Account already exists"
