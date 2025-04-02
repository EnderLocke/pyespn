## Betting Class Documentation

### Overview
The `Betting` class is responsible for handling betting-related data retrieved from ESPN. It processes betting information, including providers and futures, and associates it with an ESPN instance.

### Class Definition
```python
@validate_json("betting_json")
class Betting:
```

### Initialization
#### `__init__(self, espn_instance, betting_json)`
Initializes the `Betting` class with the given ESPN instance and betting JSON data.

- **Parameters:**
    - `espn_instance` (*object*): The ESPN instance associated with the betting data.
    - `betting_json` (*dict*): JSON data containing betting details.
- **Attributes:**
    - `betting_json`: Stores the provided betting JSON data.
    - `espn_instance`: Stores the associated ESPN instance.
    - `providers`: A list that stores betting providers.
    - `_set_betting_data()`: Called internally to populate betting data.

### Representation
#### `__repr__(self)`
Returns a string representation of the `Betting` instance.

- **Returns:**
    - `str`: A formatted string containing the betting display name and ESPN league abbreviation.

### Private Methods
#### `_set_betting_data(self)`
Extracts and assigns values from the `betting_json`.

- **Attributes Populated:**
    - `id`: The ID of the betting data.
    - `ref`: A reference to the betting data.
    - `name`: The name of the betting data.
    - `display_name`: The display name of the betting data.
    - `providers`: A list populated with `Provider` instances, created using the `futures` data from `betting_json`.

- **Functionality:**
    - Iterates through the `futures` section of `betting_json`.
    - Creates `Provider` instances for each future bet and appends them to the `providers` list.

### Example Usage
```python
espn_instance = ESPN()  # Assume ESPN instance is defined
betting_data = {...}  # JSON data containing betting information
betting = Betting(espn_instance, betting_data)
print(betting)
```

