from pyespn import PYESPN
from tests.cfb.test_cases.betting import *
import pytest

cfb_espn = PYESPN('cfb')


@pytest.mark.parametrize("test_case", champions_test_cases)
def test_champion_futures(test_case):
    content = cfb_espn.get_league_year_champion_futures(season=test_case['season'],
                                                        provider=test_case['provider'])
    test_match = content[test_case['index']]

    assert test_match['team_name'] == test_case['team_name']
    assert test_match['team_city'] == test_case['team_city']
    assert test_match['champion_future'] == test_case['line']


@pytest.mark.parametrize("test_case", conference_test_cases)
def test_conference_futures(test_case):
    content = cfb_espn.get_league_year_division_champs_futures(season=test_case['season'],
                                                               division=test_case['conference'],
                                                               provider=test_case['provider'])
    test_match = content[test_case['index']]

    assert test_match['team_name'] == test_case['team_name']
    assert test_match['team_city'] == test_case['team_city']
    assert test_match['champion_future'] == test_case['line']
    #assert test_match['team_id'] == int(test_case['team_id'])
