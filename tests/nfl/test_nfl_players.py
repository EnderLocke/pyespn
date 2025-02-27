from pyespn.nfl import get_player_info
import pytest

test_players = [
    {
        'id': 278,
        'full_name': 'Jimmy Smith',
        "dob": "1969-02-09T08:00Z",
        "type": "football",
        "debut_year": 1992,
    }
]


@pytest.mark.parametrize("test_case", test_players)
def test_nfl_events(test_case):
    content = get_player_info(test_case['id'])
    assert content['fullName'] == test_case['full_name']
    assert content['dateOfBirth'] == test_case['dob']
    assert content['type'] == test_case['type']
    assert content['debutYear'] == test_case['debut_year']
