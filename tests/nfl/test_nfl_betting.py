from pyespn.nfl import get_team_year_ats_overall, get_team_year_ml
import json
import requests
import pytest

ats_overall_test_cases = [
    {
        'season': 2020,
        'team_id': 30,
        'wins': 7,
        'losses': 9,
        'pushes': 0
    }
]

ml_test_cases = [
    {

    }
]


@pytest.mark.parametrize("test_case", ats_overall_test_cases)
def test_ats(test_case):
    content = get_team_year_ats_overall(team_id=test_case['team_id'],
                                        season=test_case['season'])
    assert content['wins'] == test_case['wins']
    assert content['losses'] == test_case['losses']
    assert content['pushes'] == test_case['pushes']



def test_ml():
    pass

