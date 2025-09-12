import networkx as nx
from networkx.readwrite import geojson

# Create a Directed Graph
G = nx.DiGraph()

# Add nodes with WKT key
G.add_node(1, geometry='POINT (0 0)')
G.add_node(2, geometry='POINT (1 0)')
G.add_node(3, geometry='POINT (1 1)')

# Add edges
G.add_edge(1, 2, weight=1.0)
G.add_edge(2, 3, weight=2.0)

# Convert nodes and edges to GeoJSON
nodes_geojson = geojson.dump(G.nodes(data=True), precision=6)
edges_geojson = geojson.dump(G.edges(data=True), precision=6)

# Write GeoJSON to shapefiles
with open('nodes.shp', 'w') as f:
    f.write(nodes_geojson)
with open('edges.shp', 'w') as f:
    f.write(edges_geojson)
