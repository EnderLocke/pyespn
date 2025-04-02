# Init the PYESPN class

## Create Class
create an init version of the class and feed it the league you want more [here](sports_available.md)

| Param   | Type               | Description               |
|---------|--------------------|---------------------------|
| league  | <code>string</code> | Options:                  |
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

## League Data
when the class is created it will try to load the league data. this will use the 
[league class](classes%2Fleague_class.md) and fill into PYESPN.league

## Teams Data
when the class is created it will try to load the teams data. this will use the
[team class](classes%2Fteams_class.md) and fill into PYESPN.teams list. it will loop thru the available teams data that is
loaded within pyespn.TEAM_ID_MAPPING and loops thru the team_ids and hits the api to pull the data. the more teams 
(i.e. college football and basketball) will take longer than leagues with lower amount of teams (i.e. nfl, nba)

