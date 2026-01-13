from typing import Any, Dict
from pyespn.utilities import fetch_espn_data


def get_pga_event_core(event_id: int) -> Dict[str, Any]:
  
    url = (
        "https://site.api.espn.com/apis/site/v2/sports/golf/leaderboard"
        f"?event={event_id}"
    )
    data = fetch_espn_data(url)

    events = data.get("events", [])
    if not events:
        raise ValueError(f"No events returned for event_id={event_id}")

    return events[0]
