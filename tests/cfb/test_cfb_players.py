from pyespn import PYESPN
from tests.cfb.test_cases.players import test_players
import pytest


@pytest.mark.parametrize("test_case", test_players)
def test_cfb_player_info(test_case):
    espn = PYESPN(sport_league='cfb')
    content = espn.get_player_info(test_case['id'])
    assert content['fullName'] == test_case['full_name']
    assert content['dateOfBirth'] == test_case['dob']
    assert content['type'] == test_case['type']
