from pyespn import PYESPN
import pytest

test_event_ids = [
    {
        'id': 401705402,
        'short_name': 'BOS @ DET',
        'name': 'Boston Celtics at Detroit Pistons',
        'date': '2025-02-27T00:00Z'
    }
]


@pytest.mark.parametrize("test_case", test_event_ids)
def test_nba_events(test_case):
    espn = PYESPN(sport_league='nba')
    content = espn.get_game_info(test_case['id'])
    assert content.short_name == test_case['short_name']
    assert content.event_name == test_case['name']
    assert content.date == test_case['date']
