from pyespn import PYESPN
from tests.f1.test_cases.standings import test_standing_cases
import pytest


@pytest.mark.parametrize("test_case", test_standing_cases)
def test_f1_standings(test_case):
    espn = PYESPN(sport_league='f1')
    content = espn.get_standings(season=test_case['season'],
                                 standings_type=test_case['standings_type'])

    this_test_match = content[test_case['index']]

    assert int(this_test_match['wins']['value']) == test_case['wins']
    assert int(this_test_match['behind']['value']) == test_case['behind']
    assert int(this_test_match['athlete_id']) == test_case['athlete_id']
