import networkx as nx
import shapefile
from shapely.geometry import Point, LineString

def create_graph_from_shapefile(shapefile_path):
    # Create an empty directed graph
    G = nx.DiGraph()

    # Read the shapefile
    sf = shapefile.Reader(shapefile_path)
    shapes = sf.shapes()
    records = sf.records()

    # Function to handle point geometries and create nodes
    def add_point_node(coords, record):
        node = tuple(coords)
        G.add_node(node)
        # Add attributes to the node
        for i, field in enumerate(sf.fields[1:]):
            G.nodes[node][field[0]] = record[i]

    # Function to handle line geometries and create edges
    def add_line_edge(coords, record):
        start_node = tuple(coords[0])
        end_node = tuple(coords[-1])
        # Simplify line geometry into start and end coordinates
        edge = (start_node, end_node)
        G.add_edge(start_node, end_node)
        # Add attributes to the edge
        for i, field in enumerate(sf.fields[1:]):
            G.edges[edge][field[0]] = record[i]

    # Iterate over the shapes and records
    for shape, record in zip(shapes, records):
        if shape.shapeType == shapefile.POINT:
            add_point_node(shape.points[0], record)
        elif shape.shapeType == shapefile.POLYLINE:
            # Simplify polylines into linestrings
            line = LineString(shape.points)
            add_line_edge(line.coords, record)

    return G
