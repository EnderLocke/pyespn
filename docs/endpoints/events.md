# Game/Event Endpoints
game/event api endpoints available

## `get_game_info(event_id)`
gets event/game details from api. the event ids can be found on the espn site web urls


| Param    | Type | Description  |
|----------| --- |--------------|
| event_id | <code>number</code> | id for event |

### Example Usage

```py
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')
event_id = 400999172 # Myles Jack wasn't down

super_bowl = nfl_espn.get_game_info(event_id=event_id)

print(super_bowl)
```

### Example Return

```json
{
    "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/400999172?lang=en&region=us",
    "id": "400999172",
    "uid": "s:20~l:28~e:400999172",
    "date": "2018-01-21T20:05Z",
    "name": "Jacksonville Jaguars at New England Patriots",
    "shortName": "JAX @ NE",
    "season": {
        "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2017?lang=en&region=us"
    },
    "seasonType": {
        "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2017/types/3?lang=en&region=us"
    },
    "week": {
        "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2017/types/3/weeks/3?lang=en&region=us"
    },
    "timeValid": true,
    ...
}
```
