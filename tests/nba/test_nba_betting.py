from pyespn import PYESPN
import pytest
from .test_cases.betting import *

nba_espn = PYESPN('nba')


@pytest.mark.parametrize('test_case', nba_champs_test_cases)
def test_nba_champs_futures(test_case):
    content = nba_espn.get_league_year_champion_futures(season=test_case['season'],
                                                        provider=test_case['provider'])
    test_match = content[test_case['index']]

    assert test_match['team_name'] == test_case['team_name']
    assert test_match['team_city'] == test_case['team_city']
    assert test_match['champion_future'] == test_case['line']


@pytest.mark.parametrize('test_case', div_champs_test_cases)
def test_west_champs_futures(test_case):
    content = nba_espn.get_league_year_division_champs_futures(season=test_case['season'],
                                                               division=test_case['division'],
                                                               provider=test_case['provider'])
    test_match = content[test_case['index']]

    assert test_match['team_name'] == test_case['team_name']
    assert test_match['team_city'] == test_case['team_city']
    assert test_match['champion_future'] == test_case['line']


