from pyespn import PYESPN
from tests.cfb.test_cases.games import test_event_cases
import pytest


@pytest.mark.parametrize("test_case", test_event_cases)
def test_cfb_events(test_case):
    espn = PYESPN(sport_league='cfb')
    content = espn.get_game_info(test_case['id'])

    assert content.short_name == test_case['short_name']
    assert content.event_name == test_case['name']
    assert content.date == test_case['date']
