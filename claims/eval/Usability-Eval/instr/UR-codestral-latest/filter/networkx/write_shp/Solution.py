import networkx as nx
import shapefile
from shapely.geometry import Point, LineString

# Create a directed graph
G = nx.DiGraph()

# Add nodes to the graph
# Nodes can have a 'wkt' or 'wkb' attribute or 'x' and 'y' attributes
G.add_node(1, wkt='POINT (10 20)')
G.add_node(2, x=30, y=40)

# Add edges to the graph
G.add_edge(1, 2)

# Function to create Point object from node attributes
def create_point(node_attributes):
    if 'wkt' in node_attributes:
        return Point(shapefile.Wkt.loads(node_attributes['wkt']))
    elif 'wkb' in node_attributes:
        return Point(shapefile.Wkb.loads(node_attributes['wkb']))
    elif 'x' in node_attributes and 'y' in node_attributes:
        return Point(node_attributes['x'], node_attributes['y'])
    else:
        raise ValueError("Invalid node attributes")

# Create shapefile for nodes
w = shapefile.Writer('nodes', shapefile.POINT)
w.field('id', 'N')
for node, attributes in G.nodes(data=True):
    w.point(create_point(attributes).x, create_point(attributes).y)
    w.record(node)
w.close()

# Create shapefile for edges
w = shapefile.Writer('edges', shapefile.POLYLINE)
w.field('start', 'N')
w.field('end', 'N')
for start, end in G.edges():
    start_point = create_point(G.nodes[start])
    end_point = create_point(G.nodes[end])
    w.line([[start_point.x, start_point.y], [end_point.x, end_point.y]])
    w.record(start, end)
w.close()
