class WaySegment():
    """ A segment of a way. """
    def __init__(self, start, stop, oneway=True):
        self.start = start
        self.stop = stop
        self.oneway = oneway
