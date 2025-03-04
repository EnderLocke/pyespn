# espn-api
work in progress for hitting hidden espn api

i am not affiliated with espn

not all api end points are available for all leagues,

i am working on adding in exceptions but you could get odd errors if say you try recruiting rankings for the nfl

please note the readme is a work in progress and there could be more api calls within the source code if you're willing to look

# Table of Contents
- [PYESPN](#pyespn)
  - [Init Class](#init-class)
  - [Data Files](#data-files)
  - [Team Data](#team-data)
  - [Player Data](#player-data)
  - [Stats Data](#stats-data)
  - [Game/Event Data](#gameevent-data)
  - [Recruiting Data](#recruiting-data)
  - [Draft Data](#draft-data)
  - [Betting Data](#betting-data)
  - [Award Data](#awards-data)
  - [Standings Data](#standings-data)
- [Team Class](#team-class)
  - []


## PYESPN
includes information on apis available for the nfl

### Init Class
create an init version of the class and feed it the league you want

| Param   | Type               | Description               |
|---------|--------------------|---------------------------|
| league  | <code>string</code> | League. Options:          |
|         |                    | - nfl                     |
|         |                    | - nba                     |
|         |                    | - wnba                    |
|         |                    | - mcbb (mens college cbb) |
|         |                    | - cfb (college football)  |
|         |                    | - cbb (college baseball)  |
|         |                    | - csb (college softball)  |
|         |                    | - f1 (formula 1)          |
|         |                    | - nascar                  |


**example**
```python
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')

```

### Data Files
This is a list of ids/teams in json format that relate to the api and are used in the code.


**examples**
```python
# this example prints the mapping itself
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')
nba_espn = PYESPN(sport_league='nba')

print(nfl_espn.TEAM_ID_MAPPING) #nfl team map
print(nba_espn.TEAM_ID_MAPPING) #nba team map
```

this example uses the [teams class](#team-class)

```python
# this example uses the teams class
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')
nba_espn = PYESPN(sport_league='nba')

for team in nfl_espn.teams:
    print(team.name) #nfl team 
    
for team in nba_espn.teams:
    print(team.name) #nba team 
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

### Player Data
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

### Stats Data
this pulls the full stats of a given player for all years in sport

#### get_players_historical_stats(player_id)
gets the historical stats for a given player id

| Param     | Type | Description   |
|-----------| --- |---------------|
| player_id | <code>number</code> | id for player |

**example**
```python
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')
player_id = 278 # Jimmy Smith, Goat

jimmy_smith_stats = nfl_espn.get_player_info(player_id=player_id)

for stat in jimmy_smith_stats:
    print(stat)
```


### Game/Event Data
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


### Recruiting Data
this pulls recruiting data and is currently only works for mcbb and cfb

| Param     | Type | Description   |
|-----------| --- |------------------|
| season | <code>number</code> | season for rankings |

**example**

```python
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')
season = 2020

recruiting_rankings = nfl_espn.get_recruiting_rankings(season=season)

for recruit in recruiting_rankings:
  print(recruit)
```



### Draft Data
Gets team info from espn api, this is available for pro leagues 

| Param      | Type | Description                        |
|------------| --- |------------------------------------|
| pick_round | <code>number</code> | round of pick                      |
| pick       | <code>number</code> | pick number in round (not overall) |
| season     | <code>number</code> | season of draft                    |

**example**
```python
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')
season = 2020
pick = 1
pick_round = 1

draft_pick_info = nfl_espn.get_draft_pick_data(pick_round=pick_round,
                                              pick=pick,
                                              season=season)

print(draft_pick_info)
```


### Betting Data

#### Betting Providers
there are many betting providers across the espn api and they dont appear to be consistant in my profiling. the ones that i have found can be accessed via

there is a mapping for default betting providers for a given sport, it is not guaranteed to return data for every year though

**example**
```python
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')

print(nfl_espn.BETTING_PROVIDERS)
```


#### Against the Spread
this appears only available for nfl

#### get_team_year_ats_away(team_id, season)
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


#### get_team_year_ats_home_favorite(team_id, season)
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


#### get_team_year_ats_away_underdog(team_id, season)
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

#### get_team_year_ats_home(team_id, season)
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

#### get_team_year_ats_overall(team_id, season)
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

#### get_team_year_ats_underdog(team_id, season)
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


#### get_team_year_ats_home_underdog(team_id, season)
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


#### Futures
api calls for futures, not available for every sport

##### get_year_league_champions_futures(season, provider)
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


##### get_league_year_division_champs_futures(season, division, provider)
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


### Awards Data
gets awards data for a given season

| Param     | Type | Description   |
|-----------| --- |------------------|
| season | <code>number</code> | season for rankings |

**example**
```python
from pyespn import PYESPN

nba_espn = PYESPN(sport_league='nba')
season = 2024

awards = nba_espn.get_standings(season=season)

for award in awards:
    print(award)
```


### Standings Data
this appears only available to racing leagues 

| Param          | Type               | Description                                     |
|---------------|--------------------|-------------------------------------------------|
| season        | <code>number</code> | Season for rankings                             |
| standings_type | <code>string</code> | Type of standings <br/>Defaults to `driver/overall` if not provided <br/>Options: |
|               |                    | **F1:** `driver`, `constructor`                |
|               |                    | **NASCAR:** `overall`                           |

**example**
```python
from pyespn import PYESPN

f1_espn = PYESPN(sport_league='f1')
season = 2024
standings_type = 'driver'

f1_standings = f1_espn.get_standings(season=season,
                                     standings_type=standings_type)

for driver in f1_standings:
    print(driver)
```


## Team Class

The `Team` class represents a sports team within the ESPN API framework. It maintains a reference
to a `PYESPN` instance to access league-specific details.

### Attributes

| Attribute | Type            | Description                                             |
|---------|-----------------|---------------------------------------------------------|
| espn_instance | <code>PYESPN</code> | Reference to the parent `PYESPN` instance.             |
| team_id | <code>number</code>     | Unique identifier for the team.                        |
| name    | <code>string</code>       | Full name of the team.                                 |
| abbreviation | <code>string</code>        | Team abbreviation (e.g., "LAL" for Los Angeles Lakers). |
| location | <code>string</code>        | Geographic location of the team (e.g., "Los Angeles"). |

### Methods

#### `get_league()`
Retrieves the league abbreviation from the associated `PYESPN` instance.

**Returns:**
- `string` — The league abbreviation (e.g., `"nfl"`, `"nba"`, `"cfb"`).

#### `__repr__()`
Returns a string representation of the `Team` instance.

**Returns:**
- `string` — A formatted string with the team's location, name, abbreviation, and league.

### Example Usage

```python
from pyespn import PYESPN

nba_espn = PYESPN(sport_league='nba')
lakers = next((team for team in nba_espn.teams if team["team_id"] == 13), None)

print(lakers)  # Output: <Team Los Angeles Lakers (LAL) - nba>
print(lakers.get_league())  # Output: nba
```
