## Event Class

### Overview
The `Event` class represents a sporting event, encapsulating details such as its name, date, venue, and other relevant metadata.

### Initialization
```python
Event(event_json)
```
#### Parameters:
- `event_json` (dict): The JSON data representing the event.

### Attributes
- `event_json` (dict): Raw event JSON data.
- `url_ref` (str): Reference URL for the event.
- `event_id` (int): Unique identifier for the event.
- `date` (str): The scheduled date and time of the event.
- `event_name` (str): The full name of the event.
- `short_name` (str): The short name of the event.
- `competition_type` (str): The type of competition.
- `venue_json` (dict): The raw JSON data for the event venue.
- `event_venue` (`Venue`): An instance of the `Venue` class representing the event's venue.
- `event_notes` (list): Notes related to the event.

### Methods
#### `__repr__()`
Returns a string representation of the `Event` instance.
```python
repr(event)
```
**Returns:**
- `str`: A formatted string containing the short name and date of the event.

#### `to_dict()`
Converts the `Event` object to a dictionary.
```python
event.to_dict()
```
**Returns:**
- `dict`: The raw event JSON data.

### Example Usage
```python
from pyespn.classes.event import Event

event_data = {
    "id": 12345,
    "date": "2025-06-15T19:00:00Z",
    "name": "Championship Game",
    "shortName": "Champ Final",
    "competitions": {
        "type": {"type": "Playoff"},
        "venue": {"id": 10, "fullName": "Stadium X"},
        "notes": ["Final match of the season"]
    }
}

event = Event(event_data)
print(event)  # Output: <Event Champ Final 2025-06-15T19:00:00Z>
print(event.to_dict())
```

