from pyespn.cfb import get_recruiting_rankings
from tests.cfb.test_cases.recruiting import recruiting_test_cases
import pytest


@pytest.mark.parametrize('test_case', recruiting_test_cases)
def test_recruit_rankings(test_case):
    content = get_recruiting_rankings(season=test_case['season'])

    test_match = content[test_case['index']]

    assert test_match['firstName'] == test_case['first_name']
    assert test_match['lastName'] == test_case['last_name']
    assert int(test_match['recruitingClass']) == test_case['season']
    assert test_match['id'] == test_case['id']
    assert test_match['position'] == test_case['position']
    assert test_match['grade'] == test_case['grade']
