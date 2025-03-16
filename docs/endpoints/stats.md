# Stats Endpoints
Available Statistics endpoints

## `get_players_historical_stats(player_id)`
gets the historical stats for a given player id

| Param     | Type | Description   |
|-----------| --- |---------------|
| player_id | <code>number</code> | id for player |

### Example Usage

```py
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')
player_id = 278 # Jimmy Smith, Goat

jimmy_smith_stats = nfl_espn.get_players_historical_stats(player_id=player_id)

for stat in jimmy_smith_stats:
    print(stat)
```
