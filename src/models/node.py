class Node():
    """ A node defines a change in the geometry of the road or an intersection. """
    def __init__(self, location, positive_id):
        self.location = location
        self.positive_id = positive_id

    def get_location_dict(self):
        """ Get the location of a node (lat/lon) as dict. """
        return {'lat' : self.location.lat, 'lon' : self.location.lon}
