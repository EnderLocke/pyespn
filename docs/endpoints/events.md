# Game/Event Endpoints
game/event api endpoints available

## `get_game_info(event_id)`
gets event/game details from api. the event ids can be found on the espn site web urls


| Param    | Type | Description  |
|----------| --- |--------------|
| event_id | <code>number</code> | id for event |

```python
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')
event_id = 401671889 # 2025 Super Bowl

super_bowl = nfl_espn.get_game_info(event_id=event_id)

print(super_bowl)
```
