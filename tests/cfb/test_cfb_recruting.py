from pyespn.cfb import get_recruiting_rankings
from tests.cfb.test_cases.recruiting import recruiting_test_cases
import pytest


@pytest.mark.parametrize('test_case', recruiting_test_cases)
def test_recruit_rankings(test_case):
    content = get_recruiting_rankings(season=test_case['season'])



    pass
