# espn-api
work in progress for hitting hidden espn api, right now there is nfl and nba functions, stay tuned for more

# Table of Contents
- [NFL](#nfl)
  - [Data Files](#data-files)
  - [Team Data](#team-data)
  - [Player Data](#player-data)
  - [Draft Data](#draft-data)
  - [Game/Event Data](#gameevent-data)
  - [Betting Data](#betting-data)
- [NBA](#nba)
  - [Data Files](#data-files-1)
  - [Team Data](#team-data-1)
  - [Player Data](#player-data-1)
  - [Draft Data](#draft-data-1)
  - [Game/Event Data](#gameevent-data-1)
  - [Betting Data](#betting-data-1)
- [CFB](#college-football--cfb)
  - [Data Files](#data-files-2)
  - [Team Data](#team-data-2)
  - [Player Data](#player-data-2)
  - [Recruiting Data](#recruiting-data)
  - [Game/Event Data](#gameevent-data-2)
  - [Betting Data](#betting-data-2)
- [MCBB](#mens-college-basketball--mcbb)


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
returns a info related toa single event

| Param   | Type | Description |
|---------| --- |-------------|
| event_id | <code>number</code> | id for event |

```python
from pyespn.nfl import get_game_info

event_id = 401671889 # 2025 Super Bowl

game_info = get_game_info(event_id=event_id)

print(game_info)
```

### Betting Data
functions under here get betting data, against the spread and futures

#### _pyespn.nfl.get_year_nfl_super_bowl_futures(season, provider) ⇒_
returns futures for superbowl winner for a given year

| Param    | Type               | Description                                      |
|----------|--------------------|--------------------------------------------------|
| season   | <code>number</code> | Year of season                                  |
| provider | <code>string</code> | Betting provider. Options:                      |
|          |                    | - DraftKings                                    |
|          |                    | - SugarHouse                                    |
|          |                    | - Caesars Sportsbook (New Jersey)               |
|          |                    | - PointsBet                                     |
|          |                    | - Caesars Sportsbook (Colorado)                 |
|          |                    | - Holland Casino                                |
|          |                    | - Caesars Sportsbook (Tennessee)                |
|          |                    | - FanDuel                                       |
|          |                    | - Unibet                                        |
|          |                    | - Bet365                                        |

```python
from pyespn.nfl import get_year_nfl_super_bowl_futures

season = 2023
provider = 'DraftKings'

futures_record = get_year_nfl_super_bowl_futures(season=season,
                                                 provider=provider)

print(futures_record)
```

#### _pyespn.nfl.get_year_nfc_division_champ_futures(season, provider) ⇒_
returns afc division champions futures

| Param    | Type               | Description                                      |
|----------|--------------------|--------------------------------------------------|
| season   | <code>number</code> | Year of season                                  |
| division | <code>string</code> | Division. Options:                              |
|          |                    | - north                                         |
|          |                    | - south                                         |
|          |                    | - west                                          |
|          |                    | - east                                          |
|          |                    | - conf                                          |
| provider | <code>string</code> | Betting provider. Options:                      |
|          |                    | - DraftKings                                    |
|          |                    | - SugarHouse                                    |
|          |                    | - Caesars Sportsbook (New Jersey)               |
|          |                    | - PointsBet                                     |
|          |                    | - Caesars Sportsbook (Colorado)                 |
|          |                    | - Holland Casino                                |
|          |                    | - Caesars Sportsbook (Tennessee)                |
|          |                    | - FanDuel                                       |
|          |                    | - Unibet                                        |
|          |                    | - Bet365                                        |

```python
from pyespn.nfl import get_year_afc_division_champ_futures

season = 2023
division = 'south'
provider = 'DraftKings'

futures_record = get_year_afc_division_champ_futures(season=season,
                                                     division=division,
                                                     provider=provider)

print(futures_record)
```

#### _pyespn.nfl.get_year_nfc_division_champ_futures(season, provider) ⇒_
returns nfc division champions futures

| Param    | Type               | Description                                      |
|----------|--------------------|--------------------------------------------------|
| season   | <code>number</code> | Year of season                                  |
| division | <code>string</code> | Division. Options:                              |
|          |                    | - north                                         |
|          |                    | - south                                         |
|          |                    | - west                                          |
|          |                    | - east                                          |
|          |                    | - conf                                          |
| provider | <code>string</code> | Betting provider. Options:                      |
|          |                    | - DraftKings                                    |
|          |                    | - SugarHouse                                    |
|          |                    | - Caesars Sportsbook (New Jersey)               |
|          |                    | - PointsBet                                     |
|          |                    | - Caesars Sportsbook (Colorado)                 |
|          |                    | - Holland Casino                                |
|          |                    | - Caesars Sportsbook (Tennessee)                |
|          |                    | - FanDuel                                       |
|          |                    | - Unibet                                        |
|          |                    | - Bet365                                        |

```python
from pyespn.nfl import get_year_nfc_division_champ_futures

season = 2023
division = 'south'
provider = 'DraftKings'

futures_record = get_year_nfc_division_champ_futures(season=season,
                                                     division=division,
                                                     provider=provider)

print(futures_record)
```

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

### Data Files

#### _pyespn.nba.data.nfl_teams_data ⇒_
This is a list of ids/teams in json format

**example**

```python
from pyespn.nba.data import nba_teams_data

print(nba_teams_data)

```

### Team Data

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

### Game/Event Data
functions under here retrieve event/game info. game id is required and is the same from espn front page

#### _pyespn.nba.get_game_info(team_id, season) ⇒_
returns a teams overall against the spread for a season

| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | id for team |
| season | <code>number</code> | year of season |

```python
from pyespn.nba import get_game_info

event_id = 401705402 # a game

game_info = get_game_info(event_id=event_id)

print(game_info)
```


### Betting Data
functions under here get betting data, against the spread

#### _pyespn.nba.get_year_nba_champ_futures(season, provider) ⇒_
returns futures for finals winner for a given year

| Param    | Type               | Description                                      |
|----------|--------------------|--------------------------------------------------|
| season   | <code>number</code> | Year of season                                  |
| provider | <code>string</code> | Betting provider. Options:                      |
|          |                    | - DraftKings                                    |
|          |                    | - SugarHouse                                    |
|          |                    | - Caesars Sportsbook (New Jersey)               |
|          |                    | - PointsBet                                     |
|          |                    | - Caesars Sportsbook (Colorado)                 |
|          |                    | - Holland Casino                                |
|          |                    | - Caesars Sportsbook (Tennessee)                |
|          |                    | - FanDuel                                       |
|          |                    | - Unibet                                        |
|          |                    | - Bet365                                        |

```python
from pyespn.nba import get_year_nba_champ_futures

season = 2023
provider = 'DraftKings'

futures_record = get_year_nba_champ_futures(season=season,
                                            provider=provider)

print(futures_record)
```

#### _pyespn.nba.get_year_east_champ_futures(season, provider) ⇒_
returns futures for east conf finals winner for a given year

| Param    | Type               | Description                                      |
|----------|--------------------|--------------------------------------------------|
| season   | <code>number</code> | Year of season                                  |
| provider | <code>string</code> | Betting provider. Options:                      |
|          |                    | - DraftKings                                    |
|          |                    | - SugarHouse                                    |
|          |                    | - Caesars Sportsbook (New Jersey)               |
|          |                    | - PointsBet                                     |
|          |                    | - Caesars Sportsbook (Colorado)                 |
|          |                    | - Holland Casino                                |
|          |                    | - Caesars Sportsbook (Tennessee)                |
|          |                    | - FanDuel                                       |
|          |                    | - Unibet                                        |
|          |                    | - Bet365                                        |

```python
from pyespn.nba import get_year_east_champ_futures

season = 2023
provider = 'DraftKings'

futures_record = get_year_east_champ_futures(season=season,
                                            provider=provider)

print(futures_record)
```

#### _pyespn.nba.get_year_west_champ_futures(season, provider) ⇒_
returns futures for west conf finals winner for a given year

| Param    | Type               | Description                                      |
|----------|--------------------|--------------------------------------------------|
| season   | <code>number</code> | Year of season                                  |
| provider | <code>string</code> | Betting provider. Options:                      |
|          |                    | - DraftKings                                    |
|          |                    | - SugarHouse                                    |
|          |                    | - Caesars Sportsbook (New Jersey)               |
|          |                    | - PointsBet                                     |
|          |                    | - Caesars Sportsbook (Colorado)                 |
|          |                    | - Holland Casino                                |
|          |                    | - Caesars Sportsbook (Tennessee)                |
|          |                    | - FanDuel                                       |
|          |                    | - Unibet                                        |
|          |                    | - Bet365                                        |

```python
from pyespn.nba import get_year_west_champ_futures

season = 2023
provider = 'DraftKings'

futures_record = get_year_west_champ_futures(season=season,
                                             provider=provider)

print(futures_record)
```

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

## College Football | CFB

### Data Files
This is the data feeds for college football - note as of 0.1.2 there are still missing values

#### _pyespn.cfb.data.cfb_teams_data ⇒_
This is a list of ids/teams in json format - currently missing values

**example**

```python
from pyespn.cfb.data import cfb_teams_data

print(cfb_teams_data)

```

### Team Data

#### _pyespn.cfb.get_team_info(team_id) ⇒_
Gets team info from espn api

| Param   | Type | Description |
|---------| --- |-------------|
| team_id | <code>number</code> | id for team |

**example**

```python
from pyespn.cfb import get_team_info

team_id = 356 # Illini

team_info = get_team_info(team_id=team_id)

print(team_info)
```

### Player Data

#### _pyespn.cfb.get_player_info(player_id) ⇒_
Gets player info from espn api

| Param     | Type | Description   |
|-----------| --- |---------------|
| player_id | <code>number</code> | id for player |

**example**

```python
from pyespn.cfb import get_player_info

player_id = 505719 # Blake Bortles, Garbage Time Goat

player_info = get_player_info(player_id=player_id)

print(player_info)
```

#### _pyespn.cfb.get_cfb_players_historical_stats(player_id) ⇒_
Gets all players stats for career

| Param     | Type | Description   |
|-----------| --- |---------------|
| player_id | <code>number</code> | id for player |

**example**

```python
from pyespn.cfb import get_cfb_players_historical_stats

player_id = 505719 # Blake Bortles, Garbage Time Goat

player_info = get_cfb_players_historical_stats(player_id=player_id)

print(player_info)
```

## College Basketball | CBB
coming ...

## MLB
coming ...

## EPL
coming ..

## F1
coming ...



