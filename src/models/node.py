class Node():
    """ A node defines a change in the geometry of the road or an intersection. """
    def __init__(self, location, positive_id):
        self.location = location
        self.positive_id = positive_id
        self.is_intersection = False

    def serialize(self):
        """ Get serialized object. """
        return {'lat' : self.location.lat, 'lon' : self.location.lon, 'is_intersection' : self.is_intersection}

    def set_is_intersection(self, value):
        """ Set is_intersection property """
        self.is_intersection = value
