# Team Class Documentation

## Overview
The `Team` class represents a sports team within the ESPN API framework. It stores team-related information and maintains a reference to a `PYESPN` instance, allowing access to league-specific details.

## Attributes

### Instance Attributes
- `espn_instance (PYESPN)`: Reference to the parent `PYESPN` instance.
- `team_id (int)`: Unique identifier for the team.
- `name (str)`: Full name of the team.
- `abbreviation (str)`: Team abbreviation (e.g., "LAL" for Los Angeles Lakers).
- `location (str)`: Geographic location of the team.
- `team_json (dict)`: Raw JSON data containing team details.

### Loaded Attributes (via `_load_team_data`)
- `guid (str)`: Unique global identifier for the team.
- `uid (str)`: Unique identifier for the team.
- `nickname (str)`: Nickname of the team.
- `display_name (str)`: Official display name of the team.
- `short_display_name (str)`: Shortened display name of the team.
- `primary_color (str)`: Primary team color (hex code).
- `alternate_color (str)`: Alternate team color (hex code).
- `is_active (bool)`: Whether the team is currently active.
- `is_all_star (bool)`: Indicates if the team is an All-Star team.
- `logos (list)`: List of logo image URLs.
- `venue_name (str)`: Name of the team's venue.
- `venue_city (str)`: City where the venue is located.
- `venue_state (str)`: State where the venue is located.
- `venue_grass (bool)`: Indicates if the venue has a grass field.
- `venue_indoors (bool)`: Indicates if the venue is an indoor facility.
- `venue_imgs (list)`: List of venue image URLs.
- `links (dict)`: Dictionary mapping link types to URLs.

## Methods

### `__init__(self, espn_instance, team_id=None, name=None, abbreviation=None, location=None, team_json=None)`
Initializes a `Team` instance.

**Parameters:**
- `espn_instance (PYESPN)`: The parent `PYESPN` instance.
- `team_id (int, optional)`: The unique identifier for the team.
- `name (str, optional)`: The name of the team.
- `abbreviation (str, optional)`: The team's abbreviation.
- `location (str, optional)`: The team's location.
- `team_json (dict, optional)`: Raw JSON data containing team details.

### `_load_team_data(self)`
Loads data from `team_json` into the `Team` instance.

### `get_logo_img(self) -> list`
Returns the list of venue images.

### `get_team_colors(self) -> dict`
Returns the team's primary and alternate colors.

**Returns:**
```json
{
    "primary_color": "#XXXXXX",
    "alt_color": "#XXXXXX"
}
```

### `get_home_venue(self) -> dict`
Returns details about the team's home venue.

**Returns:**
```json
{
    "name": "Venue Name",
    "state": "State",
    "city": "City",
    "grass": true,
    "indoor": false,
    "img_url": ["image_url_1", "image_url_2"]
}
```

### `get_league(self) -> str`
Retrieves the league abbreviation from the associated `PYESPN` instance.

**Returns:**
- `str`: The league abbreviation (e.g., "nfl", "nba", "cfb").

### `__repr__(self) -> str`
Returns a string representation of the `Team` instance.

**Returns:**
- `str`: A formatted string with the team's details.

**Example Output:**
```
<Team Los Angeles Lakers (LAL) - nba>
```

