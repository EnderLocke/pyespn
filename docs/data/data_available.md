# Available Class Data

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

this example uses the [teams_class](..%2Fclasses%2Fteams_class.md)

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
