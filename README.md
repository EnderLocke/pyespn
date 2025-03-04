# espn-api
work in progress for hitting hidden espn api, right now there is nfl and nba functions, stay tuned for more

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
  - [Game/Event Data](#gameevent-data)
  - [Recruiting Data](#recruiting-data)
  - [Draft Data](#draft-data)
  - [Betting Data](#betting-data)


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

**example**
```python
from pyespn import PYESPN

nfl_espn = PYESPN(sport_league='nfl')

print(nfl_espn.BETTING_PROVIDERS)
```


#### Against the Spread



#### Futures

### Standings Data
this appears only available to racing leagues 

| Param          | Type               | Description                                     |
|---------------|--------------------|-------------------------------------------------|
| season        | <code>number</code> | Season for rankings                             |
| standings_type | <code>string</code> | Type of standings. <br/>Defaults to `driver/overall` if not provided. <br/>Options: |
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

