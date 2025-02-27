from pyespn.nfl import get_draft_pick_data
import pytest


draft_test_cases = [
    {
        'pick': 5,
        'round': 1,
        'season': 2022,
        'traded': False,
        'athlete_id': 105533,
        'team_id': 19
    }
]


@pytest.mark.parametrize("test_case", draft_test_cases)
def test_nfl_draft(test_case):
    content = get_draft_pick_data(pick_round=test_case['round'],
                                  pick=test_case['pick'],
                                  season=test_case['season'])

    athlete_id = content['athlete']['$ref'].split('/')[content['athlete']['$ref'].split('/').index('athletes') + 1]
    team_id = content['team']['$ref'].split('/')[content['team']['$ref'].split('/').index('teams') + 1]

    assert test_case['team_id'] == team_id
    assert test_case['athlete_id'] == athlete_id
    assert test_case['traded'] == content['traded']

