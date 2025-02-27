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

print(team_info)
```

### Betting Data
functions under here get betting data, against the spread

#### _pyespn.nfl.get_team_year_ats_overall(team_id, season) ⇒_ 
returns a teams overall against the spread for a season

| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | team id. |
| season | <code>number</code> | year of season |

```python
from pyespn.nfl import get_team_year_ats_overall

team_id = 30 # JAX
season = 2020

ats_record = get_team_year_ats_overall(team_id=team_id,
                                       season=season)

print(ats_record)
```

#### _pyespn.nfl.get_team_year_ats_underdog(team_id, season) ⇒_
returns a teams against the spread for a season as an underdog

| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | team id. |
| season | <code>number</code> | year of season |

```python
from pyespn.nfl import get_team_year_ats_underdog

team_id = 30 # JAX
season = 2020

ats_record = get_team_year_ats_underdog(team_id=team_id,
                                       season=season)

print(ats_record)
```

## NBA

#### _pyespn.nba.data.nfl_teams_data ⇒_
This is a list of ids/teams in json format

**example**

```python
from pyespn.nba.data import nba_teams_data

print(nba_teams_data)

```
**examples**