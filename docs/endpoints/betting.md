# Betting Endpoints
This section contains all endpoints available for gambling data. this is not available for every league/sport

## Betting Providers
there are many betting providers across the espn api and they dont appear to be consistent in my profiling. the ones that i have found can be accessed via

there is a mapping for default betting providers for a given sport, it is not guaranteed to return data for every year though

**example**
```python
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')

print(nfl_espn.BETTING_PROVIDERS)
```


## Against the Spread Endpoints
API endpoints available for teams against the spread data, 
this appears only available for nfl

### `get_team_year_ats_away(team_id, season)`
gets a teams record against the spread while away for a season

| Param   | Type | Description         |
|---------| --- |---------------------|
| team_id | <code>number</code> | id for team         |
| season  | <code>number</code> | season for rankings |

**example**
```python
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')
season = 2024
team_id = 30 # JAX 

jax_ats = nfl_espn.get_team_year_ats_away(team_id=team_id,
                                          season=season)

print(jax_ats)
```


### `get_team_year_ats_home_favorite(team_id, season)`
gets a teams record against the spread while home favorite for a season

| Param   | Type | Description         |
|---------| --- |---------------------|
| team_id | <code>number</code> | id for team         |
| season  | <code>number</code> | season for rankings |

**example**
```python
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')
season = 2024
team_id = 30 # JAX 

jax_ats = nfl_espn.get_team_year_ats_home_favorite(team_id=team_id,
                                                   season=season)

print(jax_ats)
```


### `get_team_year_ats_away_underdog(team_id, season)`
gets a teams record against the spread while an away dog for a season

| Param   | Type | Description         |
|---------| --- |---------------------|
| team_id | <code>number</code> | id for team         |
| season  | <code>number</code> | season for rankings |

**example**
```python
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')
season = 2024
team_id = 30 # JAX 

jax_ats = nfl_espn.get_team_year_ats_away_underdog(team_id=team_id,
                                                   season=season)

print(jax_ats)
```

### `get_team_year_ats_home(team_id, season)`
gets a teams record against the spread while at home for a season

| Param   | Type | Description         |
|---------| --- |---------------------|
| team_id | <code>number</code> | id for team         |
| season  | <code>number</code> | season for rankings |

**example**
```python
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')
season = 2024
team_id = 30 # JAX 

jax_ats = nfl_espn.get_team_year_ats_home(team_id=team_id,
                                          season=season)

print(jax_ats)
```

### `get_team_year_ats_overall(team_id, season)`
gets a teams record against the spread for a season

| Param   | Type | Description         |
|---------| --- |---------------------|
| team_id | <code>number</code> | id for team         |
| season  | <code>number</code> | season for rankings |

**example**
```python
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')
season = 2024
team_id = 30 # JAX 

jax_ats = nfl_espn.get_team_year_ats_overall(team_id=team_id,
                                             season=season)

print(jax_ats)
```

### `get_team_year_ats_underdog(team_id, season)`
gets a teams record against the spread as a dog for a season

| Param   | Type | Description         |
|---------| --- |---------------------|
| team_id | <code>number</code> | id for team         |
| season  | <code>number</code> | season for rankings |

**example**
```python
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')
season = 2024
team_id = 30 # JAX 

jax_ats = nfl_espn.get_team_year_ats_underdog(team_id=team_id,
                                              season=season)

print(jax_ats)
```


### `get_team_year_ats_home_underdog(team_id, season)`
gets a teams record against the spread as a dog at home for a season

| Param   | Type | Description         |
|---------| --- |---------------------|
| team_id | <code>number</code> | id for team         |
| season  | <code>number</code> | season for rankings |

**example**
```python
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')
season = 2024
team_id = 30 # JAX 

jax_ats = nfl_espn.get_team_year_ats_home_underdog(team_id=team_id,
                                                   season=season)

print(jax_ats)
```


## Futures Endpoints
api calls for futures, not available for every sport

### `get_year_league_champions_futures(season, provider)`
gets the lines for the league champion

| Param    | Type                | Description                                                   |
|----------|---------------------|---------------------------------------------------------------|
| season   | <code>number</code> | Season for rankings.                                         |
| provider | <code>string</code> | Betting provider<br/> Options can be found in `PYESPN.BETTING_PROVIDERS`<br/> Defaults based on league if not provided. |

**example**
```python
from pyespn import PYESPN

nba_espn = PYESPN(sport_league='nba')
season = 2024

nba_futures = nba_espn.get_league_year_champion_futures(season=season)

for future in nba_futures:
    print(future)
```


### `get_league_year_division_champs_futures(season, division, provider)`
gets the lines for the specified division/conf from a provider

| Param    | Type                | Description                                                                                                                  |
|----------|---------------------|------------------------------------------------------------------------------------------------------------------------------|
| season   | <code>number</code> | Season for rankings                                                                                                          |
| division | <code>string</code> | division to get futures for<br/> Options can be found in `PYESPN.LEAGUE_DIVISION_BETTING_KEYS` |
| provider | <code>string</code> | Betting provider<br/> Options can be found in `PYESPN.BETTING_PROVIDERS`<br/> Defaults based on league if not provided.      |


**example**
```python
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nba')
season = 2024
division = 'afc'

nfl_futures = nfl_espn.get_league_year_division_champs_futures(season=season,
                                                               division=division)

for future in nfl_futures:
    print(future)
```
