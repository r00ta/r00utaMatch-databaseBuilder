from models.node import Node
from models.way import Way
from models.way_segment import WaySegment
import osmium as osm
import pandas as pd
import tempfile
import sys
import json

class OSMHandler(osm.SimpleHandler):
    def __init__(self, tmpfile):
        osm.SimpleHandler.__init__(self)
        self.nodes = {}
        self.ways = []
        self.edges = set()
        self.tmpfile = tmpfile

    def node(self, n):
        self.nodes.update({n.positive_id(): Node(n.location, n.positive_id())})

    def way(self, w):
        is_oneway = 'yes' if w.tags.get('oneway') == 'yes' else 'no'
        segments = []
        for idx in range(len(w.nodes)-1):
            segments.append(WaySegment(self.nodes[w.nodes[idx].ref], self.nodes[w.nodes[idx + 1].ref], is_oneway ))
        way = Way(segments, is_oneway)
        self.ways.append(way)

    def find_and_set_intersections(self):
        node_count = {x : 0 for x in self.nodes.keys()}
        for way in self.ways:
            for segment in way.segments:
                node_count[segment.start.positive_id] += 1
                node_count[segment.stop.positive_id] += 1
        for positive_id, count in node_count.iteritems():
            if count > 2:
                self.nodes[positive_id].is_intersection = True

    def to_json_graph(self):
        result = {}
        result.update({'nodes' : [x[1].serialize() for x in self.nodes.items()]})
        result.update({'edges' : [{'start' : segment.start.serialize(), 'stop' :
        segment.stop.serialize(), 'is_oneway' : way.is_oneway} for way in self.ways for segment in way.segments]})
        return json.dumps(result)

if __name__ == '__main__':
    tmpfile = tempfile.NamedTemporaryFile()
    osmhandler = OSMHandler(tmpfile)
    osmhandler.apply_file(sys.argv[1])
    
    osmhandler.find_and_set_intersections()
    
    print osmhandler.to_json_graph()
