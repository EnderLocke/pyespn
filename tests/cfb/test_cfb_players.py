from pyespn.cfb import get_player_info
from tests.cfb.test_cases.players import test_players
import pytest


@pytest.mark.parametrize("test_case", test_players)
def test_nfl_events(test_case):
    content = get_player_info(test_case['id'])
    assert content['fullName'] == test_case['full_name']
    assert content['dateOfBirth'] == test_case['dob']
    assert content['type'] == test_case['type']
