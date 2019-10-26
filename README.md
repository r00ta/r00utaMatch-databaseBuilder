# r00utaMatch-databaseBuilder

[![Build Status](https://dev.azure.com/r00uta/r00utaMatch/_apis/build/status/r00ta.r00utaMatch-databaseBuilder?branchName=master)](https://dev.azure.com/r00uta/r00utaMatch/_build/latest?definitionId=1&branchName=master)

Build the database from an Osm file.

Steps: 

1) Download a osm file (`map.osm`).
2) Extract all highway nodes with `osmosis --read-xml map.osm --tf accept-ways highway=* --used-node --write-xml highways.osm
3) run `src/graph_builder.py highways.osm > /tmp/test.graph`
4) use the r00utaMatch-web tool to display the graph
