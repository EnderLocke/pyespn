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
| team_id | <code>number</code> | id for team |

**example**

```python
from pyespn.nfl import get_team_info

team_id = 30 # JAX

team_info = get_team_info(team_id=team_id)

print(team_info)
```

### Player Data
these functions pull player data

#### _pyespn.nfl.get_player_info(player_id) ⇒_
Gets player info from espn api

| Param     | Type | Description   |
|-----------| --- |---------------|
| player_id | <code>number</code> | id for player |

**example**

```python
from pyespn.nfl import get_player_info

player_id = 278 # Jimmy Smith, Goat

player_info = get_player_info(player_id=player_id)

print(player_info)
```

#### _pyespn.nfl.get_nfl_players_historical_stats(player_id) ⇒_
Gets all players stats for career

| Param     | Type | Description   |
|-----------| --- |---------------|
| player_id | <code>number</code> | id for player |

**example**

```python
from pyespn.nfl import get_nfl_players_historical_stats

player_id = 278 # Jimmy Smith, Goat

player_info = get_nfl_players_historical_stats(player_id=player_id)

print(player_info)
```

### Draft Data
these functions pull data for the draft

#### _pyespn.nfl.get_draft_pick_data(team_id) ⇒_
Gets team info from espn api

| Param      | Type | Description                        |
|------------| --- |------------------------------------|
| pick_round | <code>number</code> | round of pick                      |
| pick       | <code>number</code> | pick number in round (not overall) |
| season     | <code>number</code> | season of draft                    |

**example**

```python
from pyespn.nfl import get_draft_pick_data

season = 2020
pick = 1
pick_round = 1

draft_pick_info = get_draft_pick_data(pick_round=pick_round,
                                      pick=pick,
                                      season=season)

print(draft_pick_info)
```

### Game/Event Data
functions under here retrieve event/game info. game id is required and is the same from espn front page

#### _pyespn.nfl.get_game_info(team_id, season) ⇒_
returns a teams overall against the spread for a season

| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | id for team |
| season | <code>number</code> | year of season |

```python
from pyespn.nfl import get_game_info

event_id = 401671889 # 2025 Super Bowl

game_info = get_game_info(event_id=event_id)

print(game_info)
```

### Betting Data
functions under here get betting data, against the spread

#### _pyespn.nfl.get_team_year_ats_overall(team_id, season) ⇒_ 
returns a teams overall against the spread for a season

| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | id for team |
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
| team_id | <code>number</code> | id for team |
| season | <code>number</code> | year of season |

```python
from pyespn.nfl import get_team_year_ats_underdog

team_id = 30 # JAX
season = 2020

ats_record = get_team_year_ats_underdog(team_id=team_id,
                                        season=season)

print(ats_record)
```

#### _pyespn.nfl.get_team_year_ats_away(team_id, season) ⇒_
returns a teams against the spread for a season as the away team

| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | id for team |
| season | <code>number</code> | year of season |

```python
from pyespn.nfl import get_team_year_ats_away

team_id = 30 # JAX
season = 2020

ats_record = get_team_year_ats_away(team_id=team_id,
                                    season=season)

print(ats_record)
```

#### _pyespn.nfl.get_team_year_ats_home(team_id, season) ⇒_
returns a teams against the spread for a season as the home team

| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | id for team |
| season | <code>number</code> | year of season |

```python
from pyespn.nfl import get_team_year_ats_home

team_id = 30 # JAX
season = 2020

ats_record = get_team_year_ats_home(team_id=team_id,
                                    season=season)

print(ats_record)
```

#### _pyespn.nfl.get_team_year_ats_home_favorite(team_id, season) ⇒_
returns a teams against the spread for a season as the home team and favorite

| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | id for team |
| season | <code>number</code> | year of season |

```python
from pyespn.nfl import get_team_year_ats_home_favorite

team_id = 30 # JAX
season = 2020

ats_record = get_team_year_ats_home_favorite(team_id=team_id,
                                             season=season)

print(ats_record)
```

#### _pyespn.nfl.get_team_year_ats_away_underdog(team_id, season) ⇒_
returns a teams against the spread for a season as the away team and underdog

| Param   | Type | Description    |
|---------| --- |----------------|
| team_id | <code>number</code> | id for team    |
| season | <code>number</code> | year of season |

```python
from pyespn.nfl import get_team_year_ats_away_underdog

team_id = 30 # JAX
season = 2020

ats_record = get_team_year_ats_away_underdog(team_id=team_id,
                                             season=season)

print(ats_record)
```

#### _pyespn.nfl.get_team_year_ats_home_underdog(team_id, season) ⇒_
returns a teams against the spread for a season as the home team and underdog

| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | id for team |
| season | <code>number</code> | year of season |

```python
from pyespn.nfl import get_team_year_ats_home_underdog

team_id = 30 # JAX
season = 2020

ats_record = get_team_year_ats_home_underdog(team_id=team_id,
                                             season=season)

print(ats_record)
```


## NBA

### Data Feeds

#### _pyespn.nba.data.nfl_teams_data ⇒_
This is a list of ids/teams in json format

**example**

```python
from pyespn.nba.data import nba_teams_data

print(nba_teams_data)

```

### Team Info

#### _pyespn.nba.get_team_info(team_id) ⇒_
Gets team info from espn api

| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | id for team |

**example**

```python
from pyespn.nba import get_team_info

team_id = 26 # Jazz

team_info = get_team_info(team_id=team_id)

print(team_info)
```

## Player Data
these functions pull player data

#### _pyespn.nba.get_player_info(player_id) ⇒_
Gets player info from espn api

| Param     | Type | Description   |
|-----------| --- |---------------|
| player_id | <code>number</code> | id for player |

**example**

```python
from pyespn.nba import get_player_info

player_id = 4397002 # Ayo

player_info = get_player_info(player_id=player_id)

print(player_info)
```

#### _pyespn.nba.get_nba_players_historical_stats(player_id) ⇒_
Gets all players stats for career

| Param     | Type | Description   |
|-----------| --- |---------------|
| player_id | <code>number</code> | id for player |

**example**

```python
from pyespn.nba import get_nba_players_historical_stats

player_id = 4397002 # Ayo

player_info = get_nba_players_historical_stats(player_id=player_id)

print(player_info)
```


### Betting Data
functions under here get betting data, against the spread

#### _pyespn.nba.get_team_year_ats_overall(team_id, season) ⇒_
returns a teams overall against the spread for a season

| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | id for team |
| season | <code>number</code> | year of season |

```python
from pyespn.nba import get_team_year_ats_overall

team_id = 26 # Jazz
season = 2020

ats_record = get_team_year_ats_overall(team_id=team_id,
                                       season=season)

print(ats_record)
```

#### _pyespn.nba.get_team_year_ats_underdog(team_id, season) ⇒_
returns a teams against the spread for a season as an underdog

| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | id for team |
| season | <code>number</code> | year of season |

```python
from pyespn.nba import get_team_year_ats_underdog

team_id = 26 # Jazz
season = 2020

ats_record = get_team_year_ats_underdog(team_id=team_id,
                                        season=season)

print(ats_record)
```

#### _pyespn.nba.get_team_year_ats_away(team_id, season) ⇒_
returns a teams against the spread for a season as the away team

| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | id for team |
| season | <code>number</code> | year of season |

```python
from pyespn.nba import get_team_year_ats_away

team_id = 30 # JAX
season = 2020

ats_record = get_team_year_ats_away(team_id=team_id,
                                    season=season)

print(ats_record)
```

#### _pyespn.nba.get_team_year_ats_home(team_id, season) ⇒_
returns a teams against the spread for a season as the home team

| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | id for team |
| season | <code>number</code> | year of season |

```python
from pyespn.nba import get_team_year_ats_home

team_id = 26 # Jazz
season = 2020

ats_record = get_team_year_ats_home(team_id=team_id,
                                    season=season)

print(ats_record)
```

#### _pyespn.nba.get_team_year_ats_home_favorite(team_id, season) ⇒_
returns a teams against the spread for a season as the home team and favorite

| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | id for team |
| season | <code>number</code> | year of season |

```python
from pyespn.nba import get_team_year_ats_home_favorite

team_id = 26 # Jazz
season = 2020

ats_record = get_team_year_ats_home_favorite(team_id=team_id,
                                             season=season)

print(ats_record)
```

#### _pyespn.nba.get_team_year_ats_away_underdog(team_id, season) ⇒_
returns a teams against the spread for a season as the away team and underdog

| Param   | Type | Description    |
|---------| --- |----------------|
| team_id | <code>number</code> | id for team    |
| season | <code>number</code> | year of season |

```python
from pyespn.nba import get_team_year_ats_away_underdog

team_id = 26 # Jazz
season = 2020

ats_record = get_team_year_ats_away_underdog(team_id=team_id,
                                             season=season)

print(ats_record)
```

#### _pyespn.nba.get_team_year_ats_home_underdog(team_id, season) ⇒_
returns a teams against the spread for a season as the home team and underdog

| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | id for team |
| season | <code>number</code> | year of season |

```python
from pyespn.nba import get_team_year_ats_home_underdog

team_id = 26 # Jazz
season = 2020

ats_record = get_team_year_ats_home_underdog(team_id=team_id,
                                             season=season)

print(ats_record)
```

### Draft Data
these functions pull data for the draft

#### _pyespn.nba.get_draft_pick_data(team_id) ⇒_
Gets team info from espn api

| Param      | Type | Description                        |
|------------| --- |------------------------------------|
| pick_round | <code>number</code> | round of pick                      |
| pick       | <code>number</code> | pick number in round (not overall) |
| season     | <code>number</code> | season of draft                    |

**example**

```python
from pyespn.nba import get_draft_pick_data

season = 2021
pick = 8
pick_round = 2

draft_pick_info = get_draft_pick_data(pick_round=pick_round,
                                      pick=pick,
                                      season=season)

print(draft_pick_info)
```



## MLB
coming ...

## EPL
coming ..

## F1
coming ...

## College Basketball | CBB
coming ...

## College Football | CFB
coming..

