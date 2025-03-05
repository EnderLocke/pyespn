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

### Example Usage

```py
from pyespn import PYESPN

f1_espn = PYESPN(sport_league='f1')
season = 2024
standings_type = 'driver'

f1_standings = f1_espn.get_standings(season=season,
                                     standings_type=standings_type)

for driver in f1_standings:
    print(driver)
```

### Example Return

```json
{
    "$ref": "http://sports.core.api.espn.com/v2/sports/racing/leagues/f1/seasons/2024/types/0/standings/0?lang=en&region=us",
    "id": "0",
    "name": "Driver",
    "displayName": "Driver Standings",
    "standings": [
        {
            "records": [
                {
                    "$ref": "http://sports.core.api.espn.com/v2/sports/racing/leagues/f1/seasons/2024/types/0/athletes/4665/records/0?lang=en&region=us",
                    "id": "0",
                    "name": "overall",
                    "abbreviation": "TOT",
                    "displayName": "Overall",
                    "shortDisplayName": "OVER",
                    "description": "Overall Record",
                    "type": "total",
                    "stats": [
                        {
                            "name": "wins",
                            "displayName": "Wins",
                            "shortDisplayName": "Wins",
                            "description": "Wins",
                            "abbreviation": "W",
                            "type": "wins",
                            "value": 9.0,
                            "displayValue": "9"
                        },
                        {
                            "name": "behind",
                            "displayName": "Points Behind",
                            "shortDisplayName": "Points Behind",
                            "description": "Points Behind",
                            "abbreviation": "PB",
                            "type": "behind",
                            "value": 0.0,
                            "displayValue": "0"
                        },
                        {
                            "name": "bonus",
                            "displayName": "Bonus",
                            "shortDisplayName": "Bonus",
                            "description": "Bonus",
                            "abbreviation": "BPTS",
                            "type": "bonus",
                            "value": 0.0,
                            "displayValue": "0"
                        },
                        {
                            "name": "championshipPts",
                            "displayName": "Points",
                            "shortDisplayName": "Points",
                            "description": "Championship Points",
                            "abbreviation": "PTS",
                            "type": "points",
                            "value": 437.0,
                            "displayValue": "437"
                        },
                        {
                            "name": "currentWeek",
                            "displayName": "Current Week",
                            "shortDisplayName": "Current Week",
                            "description": "Current Week",
                            "abbreviation": "CW",
                            "type": "currentweek",
                            "value": 24.0,
                            "displayValue": "24"
                        },
                        {
                            "name": "dnf",
                            "displayName": "Did Not Finish",
                            "shortDisplayName": "Did Not Finish",
                            "description": "Did Not Finish",
                            "abbreviation": "DNF",
                            "type": "dnf",
                            "value": 2.0,
                            "displayValue": "2"
                        },
                        {
                            "name": "lapsLead",
                            "displayName": "Laps Lead",
                            "shortDisplayName": "Laps Lead",
                            "description": "Laps Lead",
                            "abbreviation": "LL",
                            "type": "lapslead",
                            "value": 0.0,
                            "displayValue": "0"
                        },
                        {
                            "name": "penaltyPts",
                            "displayName": "Penalty Points",
                            "shortDisplayName": "Penalty Points",
                            "description": "Penalty Points",
                            "abbreviation": "PPTS",
                            "type": "penaltypts",
                            "value": 0.0,
                            "displayValue": "0"
                        },
                        {
                            "name": "poles",
                            "displayName": "Poles",
                            "shortDisplayName": "Poles",
                            "description": "Poles",
                            "abbreviation": "POLE",
                            "type": "poles",
                            "value": 9.0,
                            "displayValue": "9"
                        },
                        {
                            "name": "rank",
                            "displayName": "Rank",
                            "shortDisplayName": "Rank",
                            "description": "Rank",
                            "abbreviation": "RK",
                            "type": "rank",
                            "value": 1.0,
                            "displayValue": "1"
                        },
                        {
                            "name": "starts",
                            "displayName": "Starts",
                            "shortDisplayName": "Starts",
                            "description": "Starts",
                            "abbreviation": "S",
                            "type": "starts",
                            "value": 24.0,
                            "displayValue": "24"
                        },
                        {
                            "name": "top10",
                            "displayName": "Top 10",
                            "shortDisplayName": "Top 10",
                            "description": "Top 10",
                            "abbreviation": "T10",
                            "type": "top",
                            "value": 23.0,
                            "displayValue": "23"
                        },
                        {
                            "name": "top5",
                            "displayName": "Top 5",
                            "shortDisplayName": "Top 5",
                            "description": "Top 5",
                            "abbreviation": "T5",
                            "type": "top",
                            "value": 19.0,
                            "displayValue": "19"
                        },
                        {
                            "name": "topfinish",
                            "displayName": "Top Finish",
                            "shortDisplayName": "Top Finish",
                            "description": "Top finish position",
                            "abbreviation": "TF",
                            "type": "topfinish",
                            "value": 1.0,
                            "displayValue": "1"
                        },
                        {
                            "name": "totalWeeks",
                            "displayName": "Total Weeks",
                            "shortDisplayName": "Total Weeks",
                            "description": "Total Weeks",
                            "abbreviation": "TW",
                            "type": "totalweeks",
                            "value": 24.0,
                            "displayValue": "24"
                        },
                        {
                            "name": "winnings",
                            "displayName": "Winnings",
                            "shortDisplayName": "Winnings",
                            "description": "Winnings",
                            "abbreviation": "WS",
                            "type": "winnings",
                            "value": 0.0,
                            "displayValue": "0"
                        }
                    ],
                    "season": {
                        "$ref": "http://sports.core.api.espn.com/v2/sports/racing/leagues/f1/seasons/2024/types/0?lang=en&region=us"
                    }
                }
            ],
            "athlete": {
                "$ref": "http://sports.core.api.espn.com/v2/sports/racing/leagues/f1/seasons/2024/athletes/4665?lang=en&region=us"
            }
        },
      ...
  }
}
```