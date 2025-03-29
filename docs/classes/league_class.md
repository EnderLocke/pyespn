# League Class Documentation

## Overview
The `League` class is designed to represent a sports league by extracting and storing relevant data from a JSON response. This class is decorated with `@validate_json("league_json")` to ensure the input JSON data structure is valid before processing.

## Initialization
### `__init__(self, espn_instance, league_json)`
Initializes the `League` class with an ESPN API instance and a JSON object containing league details.

#### Parameters:
- `espn_instance`: An instance of the ESPN API client.
- `league_json` (dict): A dictionary containing the league information.

## Representation
### `__repr__(self)`
Returns a formatted string representation of the `League` instance, displaying the league's name.

## Attributes
Upon initialization, the `League` class extracts and sets the following attributes from the `league_json` object:

- `ref`: Reference URL or identifier for the league.
- `id`: Unique identifier for the league.
- `name`: The official name of the league.
- `display_name`: A user-friendly display name.
- `abbreviation`: Shortened abbreviation of the league.
- `short_name`: A brief name for the league.
- `slug`: A URL-friendly version of the league name.
- `is_tournament`: Boolean indicating if the league is a tournament.
- `season`: The current season's data (default: `{}`).
- `seasons`: A list of available seasons.
- `franchises`: Information about the franchises in the league.
- `teams`: List of teams participating in the league.
- `group`: A specific grouping category for the league.
- `groups`: A collection of groups associated with the league.
- `events`: List of events within the league.
- `notes`: Additional notes regarding the league.
- `rankings`: League rankings information.
- `draft`: Draft-related data for the league.
- `links`: A list of external links related to the league (default: `[]`).

## Methods
### `_set_league_json(self)`
This private method extracts and assigns values from `league_json` to the class attributes.

## Example Usage
```python
from pyespn.core.decorators import validate_json

# Assuming `espn_api` is an instance of the ESPN API client
league_data = {
    "id": 1,
    "name": "National Football League",
    "displayName": "NFL",
    "abbreviation": "NFL",
    "shortName": "NFL",
    "slug": "nfl",
    "isTournament": False,
    "season": {"year": 2024},
    "teams": [{"id": 1, "name": "New England Patriots"}]
}

league = League(espn_api, league_data)
print(league)  # Output: <League NFL>
```

## Notes
- The `League` class dynamically extracts values from `league_json`, making it adaptable to different league structures.
- Ensure `league_json` is properly structured to avoid missing attributes or incorrect mappings.

