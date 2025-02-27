from pyespn.nfl import get_game_info
import pytest

import requests
import json

test_event_ids = [
    {
        'id': 401671889,
        'short_name': 'KC VS PHI',
        'name': 'Kansas City Chiefs at Philadelphia Eagles',
        'time': '2025-02-09T23:30Z'
    }
]


def get_nfl_event_info(id):
    content = get_game_info(id)
    return content


@pytest.mark.parametrize("test_case", test_event_ids)
def test_nfl_events(test_case):
    content = get_nfl_event_info(test_case['id'])
    assert content['short_name'] == test_case['short_name']
    assert content['name'] == test_case['name']
    assert content['time'] == test_case['time']




