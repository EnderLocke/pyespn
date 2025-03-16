# Draft Endpoints
draft endpoints available

## `get_draft_pick_data(pick_round, pick, season)`
Gets team info from espn api, this is available for pro leagues

| Param      | Type | Description                        |
|------------| --- |------------------------------------|
| pick_round | <code>number</code> | round of pick                      |
| pick       | <code>number</code> | pick number in round (not overall) |
| season     | <code>number</code> | season of draft                    |

### Example Usage

```py
from pyespn import PYESPN

nba_espn = PYESPN(sport_league='nba')
season = 2021
pick = 8
pick_round = 2

draft_pick_info = nba_espn.get_draft_pick_data(pick_round=pick_round,
                                              pick=pick,
                                              season=season)

# Ayo Dosunmu
print(draft_pick_info)
```

### Example Return

```json
{
    "$ref": "http://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/seasons/2021/draft/rounds/2/picks/8?lang=en&region=us",
    "status": {
        "id": 3,
        "name": "SELECTION_MADE",
        "description": "Selection Made"
    },
    "pick": 8,
    "overall": 38,
    "round": 2,
    "traded": false,
    "athlete": {
        "$ref": "http://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/seasons/2021/draft/athletes/105080?lang=en&region=us"
    },
    "team": {
        "$ref": "http://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/seasons/2021/teams/4?lang=en&region=us"
    }
}
```