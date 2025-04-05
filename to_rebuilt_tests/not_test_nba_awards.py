from pyespn import PYESPN
from tests.nba.test_cases.awards import awards_test_cases
import pytest


@pytest.mark.parametrize("test_case", awards_test_cases)
def test_nba_awards(test_case):
    espn = PYESPN(sport_league='nba')
    content = espn.get_awards(season=test_case['season'])

    assert test_case['award'] == content['award']
    assert test_case['player_name'] == content['winner']
    assert test_case['description'] == content['award_description']
    assert test_case['position'] == content['position']
