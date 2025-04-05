from pyespn import PYESPN
from tests.test_cases.f1 import *
import pytest


f1_espn = PYESPN(sport_league='f1')


@pytest.mark.parametrize("test_case", test_standing_cases)
def test_f1_standings(test_case):
    content = f1_espn.load_standings(season=test_case['season'])

    this_test_match = content[test_case['index']]

    assert int(this_test_match['wins']['value']) == test_case['wins']
    assert int(this_test_match['behind']['value']) == test_case['behind']
    assert int(this_test_match['athlete_id']) == test_case['athlete_id']
