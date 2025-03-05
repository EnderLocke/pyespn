# Awards Endpoints
endpoints available for awards, not available for all sports

## `get_awards(season)`
gets awards data for a given season

| Param     | Type | Description   |
|-----------| --- |------------------|
| season | <code>number</code> | season for rankings |

**example**
```python
from pyespn import PYESPN

nba_espn = PYESPN(sport_league='nba')
season = 2024

awards = nba_espn.get_awards(season=season)

for award in awards:
    print(award)
```
