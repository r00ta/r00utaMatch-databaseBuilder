class Way():
    """ A way of open street map is composed by multiples segments """
    def __init__(self, segments, is_oneway=True):
        self.segments = segments
        self.is_oneway = is_oneway
