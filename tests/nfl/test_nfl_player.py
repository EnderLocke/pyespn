from pyespn import PYESPN
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
def test_nfl_players(test_case):
    nfl_pyespn = PYESPN(sport_league='nfl')
    content = nfl_pyespn.get_player_info(test_case['id'])
    assert content.full_name == test_case['full_name']
    assert content.date_of_birth == test_case['dob']
    assert content.type == test_case['type']
    assert content.debut_year == test_case['debut_year']
