from models.node import Node
from models.way import Way
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
        self.ways.append(Way(w.nodes))
        for idx in range(len(w.nodes)-1):
            self.edges.add((self.nodes[w.nodes[idx].ref], self.nodes[w.nodes[idx + 1].ref] ))

    def to_json_graph(self):
        result = {}
        result.update({'nodes' : [x[1].get_location_dict() for x in self.nodes.items()]})
        result.update({'edges' : [{'start' : x[0].get_location_dict(), 'stop' : x[1].get_location_dict()} for x in self.edges]})
        return json.dumps(result)

if __name__ == '__main__':
    tmpfile = tempfile.NamedTemporaryFile()
    osmhandler = OSMHandler(tmpfile)
    osmhandler.apply_file(sys.argv[1])

    print osmhandler.to_json_graph()
