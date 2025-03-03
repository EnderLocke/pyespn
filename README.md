# espn-api
work in progress for hitting hidden espn api, right now there is nfl and nba functions, stay tuned for more

# Table of Contents
- [PYESPN](#pyespn)
  - [Init Class](#init-class)
  - [Data Files](#data-files)
  - [Team Data](#team-data)


## PYESPN
includes information on apis available for the nfl

### Init Class
create an init veresion of the class and feed it the league you want

| Param   | Type               | Description            |
|---------|--------------------|------------------------|
| league  | <code>string</code> | League. Options:      |
|         |                    | - nfl                 |
|         |                    | - nba                 |
|         |                    | - mcbb                |
|         |                    | - cfb                 |

**example**

```python
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')

```

### Data Files

This is a list of ids/teams in json format that relate to the api and are used in the code.


**example**

```python
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')
nba_espn = PYESPN(sport_league='nba')

print(nfl_espn.TEAM_ID_MAPPING) #nfl team map
print(nba_espn.TEAM_ID_MAPPING) #nba team map
```

### Team Data
Gets team info from espn api

| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | id for team |

**example**

```python
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')
team_id = 30 #jax

jags_team_info = nfl_espn.get_team_info(team_id=team_id)

print(jags_team_info)

```




