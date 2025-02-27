from pyespn.nfl import get_draft_pick_data
import pytest


draft_test_cases = [
    {
        'pick': 8,
        'round': 2,
        'season': 2021,
        'team_id': 4,
        'traded': False,
        'athlete_id': 105080
    }
]


@pytest.mark.parametrize("test_case", draft_test_cases)
def test_nfl_draft(test_case):
    content = get_draft_pick_data(pick_round=test_case['round'],
                                  pick=test_case['pick'],
                                  season=test_case['season'])

    athlete_id = content['athlete']['$ref'].split('/')[content['athlete']['$ref'].split('/').index('athletes') + 1].split('?')[0]
    team_id = content['team']['$ref'].split('/')[content['team']['$ref'].split('/').index('teams') + 1].split('?')[0]

    assert test_case['team_id'] == int(team_id)
    assert test_case['athlete_id'] == int(athlete_id)
    assert test_case['traded'] == content['traded']

