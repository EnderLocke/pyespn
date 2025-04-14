from pyespn import PYESPN
import pytest
from tests.test_cases.nba import *

nba_espn = PYESPN('nba')


#@pytest.mark.parametrize('test_case', nba_champs_test_cases)
def no_test_nba_champs_futures(test_case):
    content = nba_espn.get_league_year_champion_futures(season=test_case['season'],
                                                        provider=test_case['provider'])
    test_match = content[test_case['index']]

    assert test_match['team_name'] == test_case['team_name']
    assert test_match['team_city'] == test_case['team_city']
    assert test_match['champion_future'] == test_case['line']


#@pytest.mark.parametrize('test_case', div_champs_test_cases)
def no_test_west_champs_futures(test_case):
    content = nba_espn.get_league_year_division_champs_futures(season=test_case['season'],
                                                               division=test_case['division'],
                                                               provider=test_case['provider'])
    test_match = content[test_case['index']]

    assert test_match['team_name'] == test_case['team_name']
    assert test_match['team_city'] == test_case['team_city']
    assert test_match['champion_future'] == test_case['line']


@pytest.mark.parametrize("test_case", draft_test_cases)
def test_nba_draft(test_case):
    content = nba_espn.get_draft_pick_data(pick_round=test_case['round'],
                                           pick=test_case['pick'],
                                           season=test_case['season'])

    athlete_id = content['athlete']['$ref'].split('/')[content['athlete']['$ref'].split('/').index('athletes') + 1].split('?')[0]
    team_id = content['team']['$ref'].split('/')[content['team']['$ref'].split('/').index('teams') + 1].split('?')[0]

    assert test_case['team_id'] == int(team_id)
    assert test_case['athlete_id'] == int(athlete_id)
    assert test_case['traded'] == content['traded']


@pytest.mark.parametrize("test_case", test_event_ids)
def test_nba_events(test_case):
    content = nba_espn.get_game_info(test_case['id'])
    assert content.short_name == test_case['short_name']
    assert content.event_name == test_case['name']
    assert content.date == test_case['date']


@pytest.mark.parametrize("test_case", test_players)
def test_nba_events(test_case):
    content = nba_espn.get_player_info(test_case['id'])
    assert content.full_name == test_case['full_name']
    assert content.date_of_birth == test_case['dob']
    assert content.type == test_case['type']


def get_random_nba_team_data(team_id):

    selected_team = next((team for team in nba_espn.team_id_mapping if team["team_id"] == team_id), None)
    content = nba_espn.get_team_by_id(team_id=team_id)

    return selected_team, content


@pytest.mark.parametrize("test_case", nba_espn.team_id_mapping)
def test_nba_team_ids(test_case):
    local_team_data, api_team_data = get_random_nba_team_data(test_case.get('team_id'))

    errors = []
    print(local_team_data.get('team_id'))
    if local_team_data['team_abbv'] != api_team_data.abbreviation:
        errors.append("Team abbreviation does not match")
    if local_team_data['team_city'] != api_team_data.location:
        errors.append("Team city does not match")
    if local_team_data['team_name'] != api_team_data.name:
        errors.append("Team name does not match")

    if errors:
        raise AssertionError("\n".join(errors))
