

class Event:

    def __init__(self, event_json):
        self.event_json = event_json
        self.url_ref = self.event_json.get('$ref')
        self.event_id = self.event_json.get('id')
        self.date = self.event_json.get('date')
        self.event_name = self.event_json.get('name')
        self.short_name = self.event_json.get('shortName')
        self.competition_type = self.event_json.get('competitions', {}).get('type', {}).get('type')


