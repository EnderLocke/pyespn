from pyespn import PYESPN
from tests.test_cases.nfl import *
import pytest

nfl_espn = PYESPN('nfl')


#@pytest.mark.parametrize("test_case", ats_overall_test_cases)
def no_test_ats_overall(test_case):
    content = nfl_espn.get_team_year_ats_overall(team_id=test_case['team_id'],
                                                 season=test_case['season'])

    assert content['wins'] == test_case['wins']
    assert content['losses'] == test_case['losses']
    assert content['pushes'] == test_case['pushes']


#@pytest.mark.parametrize("test_case", super_bowl_test_cases)
def no_test_super_bowl_futures(test_case):
    content = nfl_espn.get_league_year_champion_futures(season=test_case['season'],
                                                        provider=test_case['provider'])
    test_match = content[test_case['index']]

    assert test_match['team_name'] == test_case['team_name']
    assert test_match['team_city'] == test_case['team_city']
    assert test_match['champion_future'] == test_case['line']


#@pytest.mark.parametrize("test_case", div_test_cases)
def no_test_afc_div_futures(test_case):
    content = nfl_espn.get_league_year_division_champs_futures(season=test_case['season'],
                                                               division=test_case['division'],
                                                               provider=test_case['provider'])
    test_match = content[test_case['index']]

    assert test_match['team_name'] == test_case['team_name']
    assert test_match['team_city'] == test_case['team_city']
    assert test_match['champion_future'] == test_case['line']


@pytest.mark.parametrize("test_case", draft_test_cases)
def test_nfl_draft(test_case):
    content = nfl_espn.get_draft_pick_data(pick_round=test_case['round'],
                                           pick=test_case['pick'],
                                           season=test_case['season'])

    athlete_id = content['athlete']['$ref'].split('/')[content['athlete']['$ref'].split('/').index('athletes') + 1].split('?')[0]
    team_id = content['team']['$ref'].split('/')[content['team']['$ref'].split('/').index('teams') + 1].split('?')[0]

    assert test_case['team_id'] == int(team_id)
    assert test_case['athlete_id'] == int(athlete_id)
    assert test_case['traded'] == content['traded']


@pytest.mark.parametrize("test_case", test_event_ids)
def test_nfl_events(test_case):
    content = nfl_espn.get_game_info(test_case['id'])
    assert content.short_name == test_case['short_name']
    assert content.event_name == test_case['name']
    assert content.date == test_case['date']


@pytest.mark.parametrize("test_case", test_players)
def test_nfl_players(test_case):
    content = nfl_espn.get_player_info(test_case['id'])
    assert content.full_name == test_case['full_name']
    assert content.date_of_birth == test_case['dob']
    assert content.type == test_case['type']
    assert content.debut_year == test_case['debut_year']


@pytest.mark.parametrize('test_case', recruiting_test_cases)
@pytest.mark.xfail(strict=True)
def test_recruit_rankings(test_case):
    content = nfl_espn.get_recruiting_rankings(season=test_case['season'],
                                               max_pages=test_case['max_pages'])

    test_match = content[test_case['index']]

    assert test_match['first_name'] == test_case['first_name']
    assert test_match['last_name'] == test_case['last_name']
    assert int(test_match['class']) == test_case['season']
    assert test_match['id'] == test_case['id']
    assert test_match['position'] == test_case['position']
    assert test_match['grade'] == test_case['grade']
    assert test_match['rank'] == test_case['rank']


def get_random_nfl_team_data(team_id):
    selected_team = next((team for team in nfl_espn.team_id_mapping if team["team_id"] == team_id), None)
    content = nfl_espn.get_team_by_id(team_id)

    return selected_team, content


@pytest.mark.parametrize("test_case", nfl_espn.team_id_mapping)
def test_nfl_team_ids(test_case):
    local_team_data, api_team_data = get_random_nfl_team_data(test_case.get('team_id'))

    errors = []
    print(local_team_data.get('team_id'))

    if local_team_data['team_abbv'] != api_team_data.abbreviation:
        errors.append(f"Team abbreviation does not match")
    if local_team_data['team_city'] != api_team_data.location:
        errors.append(f"Team city does not match {local_team_data['team_city']} -> {api_team_data.location}")
    if local_team_data.get('team_name') != api_team_data.name:
        errors.append(f"Team name does not match {local_team_data['team_name']} -> {api_team_data.name}")

    if errors:
        raise AssertionError("\n".join(errors))
