from pyespn.nba import get_year_nba_champ_futures
import pytest

nba_champs_test_cases = [
    {
        'season': 2023,
        'provider': 'DraftKings',
        'team_name': 'Nuggets',
        'team_city': 'Denver',
        'line': '+475',
        'index': 0
    }
]


@pytest.mark.parametrize('test_case', nba_champs_test_cases)
def test_nba_champs_futures(test_case):
    content = get_year_nba_champ_futures(season=test_case['season'],
                                         provider=test_case['provider'])
    test_match = content[test_case['index']]

    assert test_match['team_name'] == test_case['team_name']
    assert test_match['team_city'] == test_case['team_city']
    assert test_match['champion_future'] == test_case['line']


