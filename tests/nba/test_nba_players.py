from pyespn import PYESPN
import pytest

test_players = [
    {
        'id': 4397002,
        'full_name': 'Ayo Dosunmu',
        "dob": "2000-01-17T08:00Z",
        "type": "basketball",
        "draft_year": 2021,
    }
]


@pytest.mark.parametrize("test_case", test_players)
def test_nfl_events(test_case):
    espn = PYESPN(sport_league='nba')
    content = espn.get_player_info(test_case['id'])
    assert content.full_name == test_case['full_name']
    assert content.date_of_birth == test_case['dob']
    assert content.type == test_case['type']
