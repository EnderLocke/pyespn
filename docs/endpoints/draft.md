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

nfl_espn = PYESPN(sport_league='nfl')
season = 2020
pick = 1
pick_round = 1

draft_pick_info = nfl_espn.get_draft_pick_data(pick_round=pick_round,
                                              pick=pick,
                                              season=season)

print(draft_pick_info)
```