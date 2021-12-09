import ZagreusBank.Version2.custom_exceptions as errors
from ZagreusBank.Version2.data_access_layer.implementation_classes.Account_postgres_dao import AccountPostgresDAO
from ZagreusBank.Version2.entities.Account import Account
from ZagreusBank.Version2.service_layer.implementation_services.Account_postgres_service import AccountPostgresService

account_dao = AccountPostgresDAO()
account_service = AccountPostgresService(account_dao)

account_with_duplicate_id = Account(1, 1, 200, False)


def test_catch_duplicate_account_number_for_create_method():
    try:
        account_service.service_create_account_entry(account_with_duplicate_id)
        assert False
    except errors.DuplicateAccountNumberException as e:
        assert str(e) == "Account already exists"


def test_catch_duplicate_account_number_for_update_method():
    try:
        account_service.service_update_account_information(account_with_duplicate_id)
        assert False
    except errors.DuplicateAccountNumberException as e:
        assert str(e) == "Account already exists"
