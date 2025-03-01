from pyespn.cfb import get_game_info
from tests.cfb.test_cases.games import test_event_cases
import pytest


@pytest.mark.parametrize("test_case", test_event_cases)
def test_cfb_events(test_case):
    content = get_game_info(test_case['id'])
    assert content['shortName'] == test_case['short_name']
    assert content['name'] == test_case['name']
    assert content['date'] == test_case['date']
