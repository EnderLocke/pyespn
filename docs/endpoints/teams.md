# Team Data Endpoints
available team endpoints

## `get_team_info(team_id)`
Gets team info from espn api

| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | id for team |

### Example Usage

```py
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')
team_id = 30 #jax

jags_team_info = nfl_espn.get_team_info(team_id=team_id)

print(jags_team_info)

```

### Example Return

```json
{
    "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2024/teams/30?lang=en&region=us",
    "id": "30",
    "guid": "ca6fb778-cbf6-d9a3-3e93-01230335fcab",
    "uid": "s:20~l:28~t:30",
    "alternateIds": {
        "sdr": "8814"
    },
    "slug": "jacksonville-jaguars",
    "location": "Jacksonville",
    "name": "Jaguars",
    "nickname": "Jaguars",
    "abbreviation": "JAX",
    "displayName": "Jacksonville Jaguars",
    "shortDisplayName": "Jaguars",
    "color": "007487",
    "alternateColor": "d7a22a",
    "isActive": true,
    "isAllStar": false,
    "logos": [
        {
            "href": "https://a.espncdn.com/i/teamlogos/nfl/500/jax.png",
            "width": 500,
            "height": 500,
            "alt": "",
            "rel": [
                "full",
                "default"
            ],
            "lastUpdated": "2024-06-25T18:50Z"
        },
    ],
    ...
}
```


## `get_team_colors(team_id)`
gets the alternate and primary colors for the team


| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | id for team |


```py
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')
team_id = 30 #jax

jags_colors = nfl_espn.get_team_colors(team_id=team_id)

print(jags_colors)
```

```json
{
  'alt_color': 'd7a22a', 
  'primary_color': '007487'
}
```