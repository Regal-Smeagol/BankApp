from data_access_layer.implementation_classes.team_postgres_dao import TeamPostgresDAO
from BankApp.ZagreusBank.Version2.data_access_layer.implementation_classes.Customer_postgres_dao import CustomerPostgresDAO
from entities.teams import Team
from BankApp.ZagreusBank.Version2.entities.Customer import Customer

customer_dao = CustomerPostgresDAO()

new_customer = Customer(0, "Test",  "Customer")
team_names = {'Lakers'}
team_names.add('Celtics')
team_names.add('Rockets')
team_names.add('Blazers')
new_name = team_names.pop()
update_team = Team(3, new_name)

deleted_name = team_names.pop()
delete_team = Team(0, deleted_name)


def test_create_team_success():
    team_result = customer_dao.create_team(new_customer)
    assert team_result.team_id != 0


def test_select_team_by_id_success():
    initial_team = customer_dao.get_team_by_id(1)
    assert initial_team.team_id == 1


def test_select_all_teams_success():
    teams = customer_dao.get_all_teams()
    assert len(teams) >= 3


def test_update_team_success():
    updated_team = customer_dao.update_team_information(update_team)
    assert updated_team.name == new_name


def test_delete_team_success():
    to_be_deleted = customer_dao.create_team(delete_team)
    result = customer_dao.delete_team_information(to_be_deleted.team_id)
    assert result
