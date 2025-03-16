# Player Endpoints
A List of all endpoints available that return player specific data

## `get_player_info(player_id)`
gets player level details from api

| Param     | Type | Description   |
|-----------| --- |---------------|
| player_id | <code>number</code> | id for player |

### Example Use

```py
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')
player_id = 278 # Jimmy Smith, Goat

jimmy_smith = nfl_espn.get_player_info(player_id=player_id)

print(jimmy_smith)
```

### Example Return

```json
{
    "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes/278?lang=en&region=us",
    "id": "278",
    "uid": "s:20~l:28~a:278",
    "guid": "72d3fcb1-168b-2a81-f94c-b0240bc18e79",
    "type": "football",
    "alternateIds": {
        "sdr": "1869600"
    },
    "firstName": "Jimmy",
    "lastName": "Smith",
    "fullName": "Jimmy Smith",
    "displayName": "Jimmy Smith",
    "shortName": "J. Smith",
    "weight": 202.0,
    "displayWeight": "202 lbs",
    "height": 73.0,
    "displayHeight": "6' 1\"",
    "age": 56,
    "dateOfBirth": "1969-02-09T08:00Z",
    "debutYear": 1992,
    ...
}
```
