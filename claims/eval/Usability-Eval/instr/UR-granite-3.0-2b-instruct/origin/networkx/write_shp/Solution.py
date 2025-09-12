import networkx as nx
from shapely.geometry import Point

# Assuming G is your networkx.DiGraph and nodes and edges are lists of nodes and edges respectively

# Function to convert node to shapely point
def node_to_point(node):
    return Point(node['x'], node['y'])

# Function to convert edge to shapely line string
def edge_to_line(edge):
    start_point = Point(edge['start']['x'], edge['start']['y'])
    end_point = Point(edge['end']['x'], edge['end']['y'])
    return LineString([start_point, end_point])

# Write nodes to shapefile
with open('nodes.shp', 'w') as shapefile:
    writer = shapely.wkt.Writer(shapefile)
    for node in nodes:
        if 'wkb' in node:
            writer.points.append(Point(node['wkb']))
        elif 'wkt' in node:
            writer.points.append(Point(node['wkt']))
        else:
            writer.points.append(node_to_point(node))
    writer.write()

# Write edges to shapefile
with open('edges.shp', 'w') as shapefile:
    writer = shapely.wkt.Writer(shapefile)
    for edge in edges:
        writer.lines.append(edge_to_line(edge))
    writer.write()
