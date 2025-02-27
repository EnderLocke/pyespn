# espn-api

work in progress for hitting hidden espn api, more to come

## NFL
includes information on apis available for the nfl

### Data Files

#### _pyespn.nfl.data.nfl_teams_data ⇒_
This is a list of ids/teams in json format

**example**

```python
from pyespn.nfl.data import nfl_teams_data

print(nfl_teams_data)

```
### Team Data
functions under here get team data

#### _pyespn.nfl.get_team_info(team_id) ⇒_
Gets team info from espn api

| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | team id. |

**examples**

```python
from pyespn.nfl import get_team_info

team_id = 30 # JAX

team_info = get_team_info(team_id=team_id)

```

### Betting Data
functions under here get betting data, against the spread

#### _pyespn.nfl.get_team_ats_overall(team_id, season) ⇒_ 
returns a teams overall against the spread for a season

| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | team id. |
| season | <code>number</code> | year of season |

```python

```


## NBA

**examples**