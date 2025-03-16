# Awards Endpoints
endpoints available for awards, not available for all sports

## `get_awards(season)`
gets awards data for a given season

| Param     | Type | Description   |
|-----------| --- |------------------|
| season | <code>number</code> | season for rankings |

### Example Usage

```py
from pyespn import PYESPN

nba_espn = PYESPN(sport_league='nba')
season = 2024

awards = nba_espn.get_awards(season=season)

for award in awards:
    print(award)
```

### Example Return

```json
[
  {
    'athlete_id': 3112335,
    'award': 'MVP',
    'award_description': 'NBA Most Valuable Player',
    'winner': 'Nikola Jokic',
    'position': 'C'
  },
  {
    'athlete_id': 3032976,
    'award': 'Defensive Player of the Year',
    'award_description': 'NBA Defensive Player of the Year',
    'winner': 'Rudy Gobert',
    'position': 'C'
  },
  {
    'athlete_id': 4432816,
    'award': 'Rookie of the Year',
    'award_description': 'NBA Rookie of the Year',
    'winner': 'LaMelo Ball',
    'position': 'PG'
  },
  {
    'athlete_id': 2528426,
    'award': 'Sixth Man of the Year',
    'award_description': 'NBA Sixth Man Award',
    'winner': 'Jordan Clarkson',
    'position': 'PG'
  },
  {
    'athlete_id': 3064514,
    'award': 'Most Improved Player',
    'award_description': 'NBA Most Improved Player',
    'winner': 'Julius Randle',
    'position': 'PF'
  },
  {
    'athlete_id': 3032977,
    'award': 'Finals MVP',
    'award_description': 'NBA Finals Most Valuable Player',
    'winner': 'Giannis Antetokounmpo',
    'position': 'PF'
  },
  {
    'athlete_id': 3975,
    'award': 'All-NBA 1st Team',
    'award_description': 'All-NBA First Team',
    'winner': 'Stephen Curry',
    'position': 'PG'
  },
  {
    'athlete_id': 6450,
    'award': 'All-NBA 1st Team',
    'award_description': 'All-NBA First Team',
    'winner': 'Kawhi Leonard',
    'position': 'SF'
  },
  {
    'athlete_id': 3032977,
    'award': 'All-NBA 1st Team',
    'award_description': 'All-NBA First Team',
    'winner': 'Giannis Antetokounmpo',
    'position': 'PF'
  },
  {
    'athlete_id': 3112335,
    'award': 'All-NBA 1st Team',
    'award_description': 'All-NBA First Team',
    'winner': 'Nikola Jokic',
    'position': 'C'
  },
  {
    'athlete_id': 3945274,
    'award': 'All-NBA 1st Team',
    'award_description': 'All-NBA First Team',
    'winner': 'Luka Doncic',
    'position': 'PG'
  },
  {
    'athlete_id': 1966,
    'award': 'All-NBA 2nd Team',
    'award_description': 'All-NBA Second Team',
    'winner': 'LeBron James',
    'position': 'SF'
  },
  {
    'athlete_id': 2779,
    'award': 'All-NBA 2nd Team',
    'award_description': 'All-NBA Second Team',
    'winner': 'Chris Paul',
    'position': 'PG'
  },
  {
    'athlete_id': 6606,
    'award': 'All-NBA 2nd Team',
    'award_description': 'All-NBA Second Team',
    'winner': 'Damian Lillard',
    'position': 'PG'
  },
  {
    'athlete_id': 3059318,
    'award': 'All-NBA 2nd Team',
    'award_description': 'All-NBA Second Team',
    'winner': 'Joel Embiid',
    'position': 'C'
  },
  {
    'athlete_id': 3064514,
    'award': 'All-NBA 2nd Team',
    'award_description': 'All-NBA Second Team',
    'winner': 'Julius Randle',
    'position': 'PF'
  },
  {
    'athlete_id': 4251,
    'award': 'All-NBA 3rd Team',
    'award_description': 'All-NBA Third Team',
    'winner': 'Paul George',
    'position': 'F'
  },
  {
    'athlete_id': 6430,
    'award': 'All-NBA 3rd Team',
    'award_description': 'All-NBA Third Team',
    'winner': 'Jimmy Butler III',
    'position': 'SF'
  },
  {
    'athlete_id': 6442,
    'award': 'All-NBA 3rd Team',
    'award_description': 'All-NBA Third Team',
    'winner': 'Kyrie Irving',
    'position': 'PG'
  },
  {
    'athlete_id': 6580,
    'award': 'All-NBA 3rd Team',
    'award_description': 'All-NBA Third Team',
    'winner': 'Bradley Beal',
    'position': 'SG'
  },
  {
    'athlete_id': 3032976,
    'award': 'All-NBA 3rd Team',
    'award_description': 'All-NBA Third Team',
    'winner': 'Rudy Gobert',
    'position': 'C'
  },
  {
    'athlete_id': 3136777,
    'award': 'All-Rookie 1st Team',
    'award_description': 'NBA All-Rookie First Team',
    'winner': "Jae'Sean Tate",
    'position': 'SF'
  },
  {
    'athlete_id': 4396993,
    'award': 'All-Rookie 1st Team',
    'award_description': 'NBA All-Rookie First Team',
    'winner': 'Tyrese Haliburton',
    'position': 'PG'
  },
  {
    'athlete_id': 4397136,
    'award': 'All-Rookie 1st Team',
    'award_description': 'NBA All-Rookie First Team',
    'winner': 'Saddiq Bey',
    'position': 'SF'
  },
  {
    'athlete_id': 4432816,
    'award': 'All-Rookie 1st Team',
    'award_description': 'NBA All-Rookie First Team',
    'winner': 'LaMelo Ball',
    'position': 'PG'
  },
  {
    'athlete_id': 4594268,
    'award': 'All-Rookie 1st Team',
    'award_description': 'NBA All-Rookie First Team',
    'winner': 'Anthony Edwards',
    'position': 'SG'
  },
  {
    'athlete_id': 4066320,
    'award': 'All-Rookie 2nd Team',
    'award_description': 'NBA All-Rookie Second Team',
    'winner': 'Desmond Bane',
    'position': 'SG'
  },
  {
    'athlete_id': 4395724,
    'award': 'All-Rookie 2nd Team',
    'award_description': 'NBA All-Rookie Second Team',
    'winner': 'Immanuel Quickley',
    'position': 'SG'
  },
  {
    'athlete_id': 4431687,
    'award': 'All-Rookie 2nd Team',
    'award_description': 'NBA All-Rookie Second Team',
    'winner': 'Patrick Williams',
    'position': 'PF'
  },
  {
    'athlete_id': 4432810,
    'award': 'All-Rookie 2nd Team',
    'award_description': 'NBA All-Rookie Second Team',
    'winner': 'Isaiah Stewart',
    'position': 'C'
  },
  {
    'athlete_id': 4432822,
    'award': 'All-Rookie 2nd Team',
    'award_description': 'NBA All-Rookie Second Team',
    'winner': 'Isaac Okoro',
    'position': 'SF'
  },
  {
    'athlete_id': 3995,
    'award': 'All-Defensive 1st Team',
    'award_description': 'NBA All-Defensive First Team',
    'winner': 'Jrue Holiday',
    'position': 'PG'
  },
  {
    'athlete_id': 6589,
    'award': 'All-Defensive 1st Team',
    'award_description': 'NBA All-Defensive First Team',
    'winner': 'Draymond Green',
    'position': 'PF'
  },
  {
    'athlete_id': 3032976,
    'award': 'All-Defensive 1st Team',
    'award_description': 'NBA All-Defensive First Team',
    'winner': 'Rudy Gobert',
    'position': 'C'
  },
  {
    'athlete_id': 3032977,
    'award': 'All-Defensive 1st Team',
    'award_description': 'NBA All-Defensive First Team',
    'winner': 'Giannis Antetokounmpo',
    'position': 'PF'
  },
  {
    'athlete_id': 3907387,
    'award': 'All-Defensive 1st Team',
    'award_description': 'NBA All-Defensive First Team',
    'winner': 'Ben Simmons',
    'position': 'PG'
  },
  {
    'athlete_id': 6430,
    'award': 'All-Defensive 2nd Team',
    'award_description': 'NBA All-Defensive Second Team',
    'winner': 'Jimmy Butler III',
    'position': 'SF'
  },
  {
    'athlete_id': 6450,
    'award': 'All-Defensive 2nd Team',
    'award_description': 'NBA All-Defensive Second Team',
    'winner': 'Kawhi Leonard',
    'position': 'SF'
  },
  {
    'athlete_id': 3059318,
    'award': 'All-Defensive 2nd Team',
    'award_description': 'NBA All-Defensive Second Team',
    'winner': 'Joel Embiid',
    'position': 'C'
  },
  {
    'athlete_id': 3907498,
    'award': 'All-Defensive 2nd Team',
    'award_description': 'NBA All-Defensive Second Team',
    'winner': 'Matisse Thybulle',
    'position': 'SG'
  },
  {
    'athlete_id': 4066261,
    'award': 'All-Defensive 2nd Team',
    'award_description': 'NBA All-Defensive Second Team',
    'winner': 'Bam Adebayo',
    'position': 'C'
  },
  {
    'athlete_id': 3032977,
    'award': 'All-Star MVP',
    'award_description': 'All-Star Most Valuable Player',
    'winner': 'Giannis Antetokounmpo',
    'position': 'PF'
  },
  {
    'athlete_id': 6606,
    'award': 'Twyman-Stokes Teammate of the Year Award',
    'award_description': 'Twyman-Stokes Teammate of the Year Award',
    'winner': 'Damian Lillard',
    'position': 'PG'
  }
]

```