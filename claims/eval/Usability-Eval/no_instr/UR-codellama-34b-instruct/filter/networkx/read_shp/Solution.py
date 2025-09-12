
import networkx as nx
from shapely.geometry import Point, LineString
from shapely.ops import transform

def generate_graph(shapefile):
    """
    Generates a networkx.DiGraph from a shapefile.
    Point geometries are translated into nodes, lines into edges.
    Coordinate tuples are used as keys.
    Attributes are preserved, line geometries are simplified into start and end coordinates.
    Accepts a single shapefile or directory of many shapefiles.
    """
    # Load the shapefile using Fiona
    with fiona.open(shapefile) as source:
        features = list(source)
    
    # Create an empty graph
    G = nx.DiGraph()
    
    # Iterate over each feature in the shapefile
    for feature in features:
        # Check if the feature is a point geometry
        if feature["geometry"]["type"] == "Point":
            # Add a node to the graph with the coordinates of the point as the key
            G.add_node(feature["properties"]["ID"], feature["geometry"].coords[0])
        
        # Check if the feature is a line geometry
        elif feature["geometry"]["type"] == "LineString":
            # Add an edge to the graph with the start and end coordinates of the line as the keys
            G.add_edge(feature["properties"]["ID"], (feature["geometry"].coords[0], feature["geometry"].coords[-1]))
    
    return G
