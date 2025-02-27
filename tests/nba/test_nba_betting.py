from pyespn.nba import get_year_nba_champ_futures, get_year_west_champ_futures, get_year_east_champ_futures
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

west_champs_test_cases = [
    {
        'season': 2023,
        'provider': 'DraftKings',
        'team_name': 'Nuggets',
        'team_city': 'Denver',
        'line': '+250',
        'index': 0
    }
]

east_champs_test_cases = [
    {
        'season': 2023,
        'provider': 'DraftKings',
        'team_name': 'Celtics',
        'team_city': 'Boston',
        'line': '+210',
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


@pytest.mark.parametrize('test_case', west_champs_test_cases)
def test_west_champs_futures(test_case):
    content = get_year_west_champ_futures(season=test_case['season'],
                                          provider=test_case['provider'])
    test_match = content[test_case['index']]

    assert test_match['team_name'] == test_case['team_name']
    assert test_match['team_city'] == test_case['team_city']
    assert test_match['champion_future'] == test_case['line']


@pytest.mark.parametrize('test_case', east_champs_test_cases)
def test_east_champs_futures(test_case):
    content = get_year_east_champ_futures(season=test_case['season'],
                                          provider=test_case['provider'])
    test_match = content[test_case['index']]

    assert test_match['team_name'] == test_case['team_name']
    assert test_match['team_city'] == test_case['team_city']
    assert test_match['champion_future'] == test_case['line']

