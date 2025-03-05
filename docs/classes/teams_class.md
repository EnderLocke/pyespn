# Team Class

The `Team` class represents a sports team within the ESPN API framework. It maintains a reference
to a `PYESPN` instance to access league-specific details.

## Attributes

| Attribute | Type            | Description                                             |
|---------|-----------------|---------------------------------------------------------|
| espn_instance | <code>PYESPN</code> | Reference to the parent `PYESPN` instance.             |
| team_id | <code>number</code>     | Unique identifier for the team.                        |
| name    | <code>string</code>       | Full name of the team.                                 |
| abbreviation | <code>string</code>        | Team abbreviation (e.g., "LAL" for Los Angeles Lakers). |
| location | <code>string</code>        | Geographic location of the team (e.g., "Los Angeles"). |

## Methods

### `get_league()`
Retrieves the league abbreviation from the associated `PYESPN` instance.

**Returns:**
- `string` — The league abbreviation (e.g., `"nfl"`, `"nba"`, `"cfb"`).

### `__repr__()`
Returns a string representation of the `Team` instance.

**Returns:**
- `string` — A formatted string with the team's location, name, abbreviation, and league.

## Example Usage

```python
from pyespn import PYESPN

nba_espn = PYESPN(sport_league='nba')
lakers = next((team for team in nba_espn.teams if team["team_id"] == 13), None)

print(lakers)  # Output: <Team Los Angeles Lakers (LAL) - nba>
print(lakers.get_league())  # Output: nba
```

