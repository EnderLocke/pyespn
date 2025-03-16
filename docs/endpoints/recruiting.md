# Recruiting Endpoints
Recruiting endpoints available


## `get_recruiting_rankings(season)`
this pulls recruiting data and is currently only works for mcbb and cfb


| Param     | Type | Description   |
|-----------| --- |------------------|
| season | <code>number</code> | season for rankings |

### Example Usage

```py
from pyespn import PYESPN

cfb_espn = PYESPN(sport_league='cfb')
season = 2020

recruiting_rankings = cfb_espn.get_recruiting_rankings(season=season)

for recruit in recruiting_rankings:
  print(recruit)
```

### Example Return

*api url*
```
https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/recruiting/2022/athletes
```

```json
{
  "count": 3467,
  "pageIndex": 1,
  "pageSize": 25,
  "pageCount": 139,
  "items": [
    {
      "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/recruits/240611?lang=en&region=us",
      "athlete": {
        "id": "240611",
        "alternateId": "4685503",
        "firstName": "Walter",
        "lastName": "Nolen",
        "fullName": "Walter Nolen",
        "displayName": "Walter Nolen",
        "shortName": "W. Nolen",
        "weight": 325.0,
        "height": 76.0,
        "links": [
          {
            "language": "en-US",
            "rel": [
              "playercard",
              "desktop",
              "recruitathlete"
            ],
            "href": "https://www.espn.com/college-sports/football/recruiting/player/_/id/240611",
            "text": "Player Card",
            "shortText": "Player Card",
            "isExternal": false,
            "isPremium": false
          }
        ],
        "highSchool": {
          "id": "11056",
          "name": "Powell High School",
          "properName": "Powell High School",
          "address": {
            "city": "Powell",
            "state": "Tennessee",
            "stateAbbreviation": "TN",
            "address1": "2136 West Emory Rd",
            "zipCode": "37849"
          }
        },
        "hometown": {
          "city": "Powell",
          "state": "Tennessee",
          "stateAbbreviation": "TN"
        },
        "position": {
          "id": "7",
          "abbreviation": "DT"
        }
      },
      "recruitingClass": 2022,
      "status": {
        "id": 3,
        "description": "Signed"
      },
      "grade": 95,
      "gradeDisplayValue": "95",
      "attributes": [
        {
          "type": 1,
          "name": "rank",
          "displayName": "Rank",
          "abbreviation": "RK",
          "value": 1.0,
          "displayValue": "1"
        },
        {
          "type": 2,
          "name": "positionRank",
          "displayName": "Position Rank",
          "abbreviation": "POS RK",
          "value": 1.0,
          "displayValue": "1"
        },
        {
          "type": 3,
          "name": "stateRank",
          "displayName": "State Rank",
          "abbreviation": "STA RK",
          "value": 1.0,
          "displayValue": "1"
        },
        {
          "type": 4,
          "name": "regionRank",
          "displayName": "Region Rank",
          "abbreviation": "REG RK",
          "value": 1.0,
          "displayValue": "1"
        },
        {
          "type": 5,
          "name": "fortyYrdDash",
          "displayName": "40-Yard Dash",
          "abbreviation": "40 YD",
          "value": 99.0,
          "displayValue": "99"
        },
        {
          "type": 6,
          "name": "threeConeDrill",
          "displayName": "3-Cone Drill",
          "abbreviation": "3 CD",
          "value": 99.0,
          "displayValue": "99"
        },
        {
          "type": 7,
          "name": "twentyYrdShuttle",
          "displayName": "20-Yard Shuttle",
          "abbreviation": "20 YS",
          "value": 99.0,
          "displayValue": "99"
        }
      ],
      "analysis": [
        {
          "id": "99",
          "type": "raw"
        }
      ],
      "schools": [
          ...
      ]
    },
  ...
```
