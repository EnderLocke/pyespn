from pyespn import PYESPN
from tests.nfl.test_cases.betting import *
import pytest

nfl_espn = PYESPN('nfl')

ats_overall_test_cases = [
    {
        'season': 2020,
        'team_id': 30,
        'wins': 7,
        'losses': 9,
        'pushes': 0
    }
]


@pytest.mark.parametrize("test_case", ats_overall_test_cases)
def test_ats_overall(test_case):
    content = nfl_espn.get_team_year_ats_overall(team_id=test_case['team_id'],
                                                 season=test_case['season'])

    assert content['wins'] == test_case['wins']
    assert content['losses'] == test_case['losses']
    assert content['pushes'] == test_case['pushes']


@pytest.mark.parametrize("test_case", super_bowl_test_cases)
def test_super_bowl_futures(test_case):
    content = nfl_espn.get_league_year_champion_futures(season=test_case['season'],
                                                        provider=test_case['provider'])
    test_match = content[test_case['index']]

    assert test_match['team_name'] == test_case['team_name']
    assert test_match['team_city'] == test_case['team_city']
    assert test_match['champion_future'] == test_case['line']


@pytest.mark.parametrize("test_case", div_test_cases)
def test_afc_div_futures(test_case):
    content = nfl_espn.get_league_year_division_champs_futures(season=test_case['season'],
                                                               division=test_case['division'],
                                                               provider=test_case['provider'])
    test_match = content[test_case['index']]

    assert test_match['team_name'] == test_case['team_name']
    assert test_match['team_city'] == test_case['team_city']
    assert test_match['champion_future'] == test_case['line']


def test_ml():
    pass

