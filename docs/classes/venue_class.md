## Venue Class

### Description
The `Venue` class is designed to store and manage information about a sports venue. It extracts data from a given JSON structure and provides methods to access and represent the venue information.

### Initialization
```python
Venue(venue_json)
```
- **venue_json** (*dict*): A dictionary containing venue data.

### Attributes
- **venue_json** (*dict*): The original JSON data provided during initialization.
- **venue_id** (*int*): The unique identifier of the venue.
- **name** (*str*): The full name of the venue.
- **address_json** (*dict*): The address details of the venue.
- **grass** (*bool*): Indicates whether the venue has a grass surface.
- **indoor** (*bool*): Indicates whether the venue is an indoor facility.
- **images** (*list*): A list of image URLs related to the venue.

### Methods
#### `__repr__()`
```python
__repr__() -> str
```
Returns a string representation of the venue instance.

- **Returns:**
    - (*str*): A formatted string displaying the venue's name.

#### `to_dict()`
```python
to_dict() -> dict
```
Returns the venue's data as a dictionary.

- **Returns:**
    - (*dict*): The original venue JSON data.

### Example Usage
```python
venue_data = {
    "id": 123,
    "fullName": "Stadium X",
    "address": {"city": "Somewhere", "state": "NY"},
    "grass": True,
    "indoor": False,
    "images": ["image1.jpg", "image2.jpg"]
}

venue = Venue(venue_data)
print(venue)  # Output: <Venue Stadium X>
print(venue.to_dict())  # Returns the original venue JSON data
```

