class Node():
    def __init__(self, location, positive_id):
        self.location = location
        self.positive_id = positive_id

    def get_location_dict(self):
        return {'lat' : self.location.lat, 'lon' : self.location.lon}
