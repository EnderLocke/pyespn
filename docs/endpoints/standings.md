# Standings Endpoints
endpoints to get standings 

## `get_standings(season, standings_type)`
get standings for a given season, this appears only available to racing leagues

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
