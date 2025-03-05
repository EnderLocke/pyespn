# Recruiting Endpoints
Recruiting endpoints available


## `get_recruiting_rankings(season)`
this pulls recruiting data and is currently only works for mcbb and cfb


| Param     | Type | Description   |
|-----------| --- |------------------|
| season | <code>number</code> | season for rankings |

**example**

```py
from pyespn import PYESPN

cfb_espn = PYESPN(sport_league='cfb')
season = 2020

recruiting_rankings = cfb_espn.get_recruiting_rankings(season=season)

for recruit in recruiting_rankings:
  print(recruit)
```
