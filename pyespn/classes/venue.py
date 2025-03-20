

class Venue:

    def __init__(self, venue_json):
        self.venue_json = venue_json
        self.venue_id = self.venue_json.get('id')
        self.name = self.venue_json.get('fullName')
        self.address_json = self.venue_json.get('address')
        self.grass = self.venue_json.get('grass')
        self.indoor = self.venue_json.get('indoor')
        self.images = self.venue_json.get('images', [])
