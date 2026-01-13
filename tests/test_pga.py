from pyespn import PYESPN
import pytest
from tests.test_cases.pga import event_test_cases, athlete_test_cases

pga_espn = PYESPN("pga")

@pytest.mark.parametrize("case", event_test_cases)
def test_pga_event_metadata(case):
    ev = pga_espn.get_pga_event(case["event_id"])
    assert int(ev["id"]) == case["event_id"]
    assert ev["name"] == case["name"]
    assert ev["season"]["year"] == case["season"]
    assert ev["status"]["type"]["state"] == case["status_state"]
    assert ev["status"]["type"]["description"] == case["status_description"]


@pytest.mark.parametrize("case", athlete_test_cases)
def test_pga_defending_champion(case):
    ev = pga_espn.get_pga_event(case["event_id"])
    champ = ev["defendingChampion"]["athlete"]
    assert int(champ["id"]) == case["id"]
    assert champ["displayName"] == case["display_name"]

