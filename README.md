# espn-api

work in progress for hitting hidden espn api, more to come

## NFL
includes information on apis available for the nfl

### pyespn.nfl.get_team_info(team_id) ⇒
Gets team info from espn api

| Param | Type | Description |
| --- | --- |-------------|
| id | <code>number</code> | team id. |

**examples**
```python
from pyespn.nfl import get_team_info

team_id = 30 # JAX

team_info = get_team_info(team_id=team_id)

```

## NBA

**examples**