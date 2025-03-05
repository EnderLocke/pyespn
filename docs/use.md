# Init the PYESPN class

## Create Class
create an init version of the class and feed it the league you want

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