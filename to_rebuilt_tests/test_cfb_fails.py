from pyespn import PYESPN
from tests.cfb.test_cases.betting import *
import pytest


@pytest.mark.parametrize("test_case", champions_test_cases)
@pytest.mark.xfail(strict=True)
def test_champion_futures(test_case):
    cfb_espn = PYESPN('lol')
    content = cfb_espn.get_league_year_champion_futures(season=test_case['season'],
                                                        provider=test_case['provider'])
    test_match = content[test_case['index']]

    assert test_match['team_name'] == test_case['team_name']
    assert test_match['team_city'] == test_case['team_city']
    assert test_match['champion_future'] == test_case['line']
