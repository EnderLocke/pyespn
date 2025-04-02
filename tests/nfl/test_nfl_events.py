from pyespn import PYESPN
import pytest

test_event_ids = [
    {
        'id': 401671889,
        'short_name': 'KC VS PHI',
        'name': 'Kansas City Chiefs at Philadelphia Eagles',
        'date': '2025-02-09T23:30Z'
    }
]


@pytest.mark.parametrize("test_case", test_event_ids)
def test_nfl_events(test_case):
    espn = PYESPN(sport_league='nfl')
    content = espn.get_game_info(test_case['id'])
    assert content.short_name == test_case['short_name']
    assert content.event_name == test_case['name']
    assert content.date == test_case['date']




