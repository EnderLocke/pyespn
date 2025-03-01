from pyespn.cfb import (get_year_cfb_champions_futures,
                        get_year_conference_champ_futures)
from pyespn.utilities import get_team_id
from tests.cfb.test_cases.betting import *
import pytest


@pytest.mark.parametrize("test_case", champions_test_cases)
def test_champion_futures(test_case):
    content = get_year_cfb_champions_futures(season=test_case['season'],
                                             provider=test_case['provider'])
    test_match = content[test_case['index']]

    assert test_match['team_name'] == test_case['team_name']
    assert test_match['team_city'] == test_case['team_city']
    assert test_match['champion_future'] == test_case['line']


@pytest.mark.parametrize("test_case", conference_test_cases)
def test_conference_futures(test_case):
    content = get_year_conference_champ_futures(season=test_case['season'],
                                                conference=test_case['conference'],
                                                provider=test_case['provider'])
    test_match = content[test_case['index']]
    #team_id = get_team_id(test_match['team']['$ref'])

    assert test_match['team_name'] == test_case['team_name']
    assert test_match['team_city'] == test_case['team_city']
    assert test_match['champion_future'] == test_case['line']
    #assert team_id == int(test_case['team_id'])
