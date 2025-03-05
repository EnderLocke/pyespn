# Team Data Endpoints
available team endpoints

## `get_team_info`
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
