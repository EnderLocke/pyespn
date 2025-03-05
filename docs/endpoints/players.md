# Player Endpoints
player endpoints available

## `get_player_info`
gets player level details from api

| Param     | Type | Description   |
|-----------| --- |---------------|
| player_id | <code>number</code> | id for player |

**example**
```python
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')
player_id = 278 # Jimmy Smith, Goat

jimmy_smith = nfl_espn.get_player_info(player_id=player_id)

print(jimmy_smith)
```
