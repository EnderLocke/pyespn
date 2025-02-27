from pyespn.nba import get_game_info
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
    content = get_game_info(test_case['id'])
    assert content['shortName'] == test_case['short_name']
    assert content['name'] == test_case['name']
    assert content['date'] == test_case['date']
