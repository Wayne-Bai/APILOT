import networkx as nx
from shapely.geometry import shape
import fiona

# Function to create a graph from a shapefile
def graph_from_shapefile(filename):
    # Open the shapefile and read the features
    with fiona.open(filename, 'r') as shapefile:
        features = [feature for feature in shapefile]

    # Create a new graph
    G = nx.DiGraph()

    # Add nodes for each point geometry and store attributes as node properties
    for feature in features:
        if feature['geometry']['type'] == 'Point':
            G.add_node(tuple(feature['geometry']['coordinates']), **feature['properties'])

    # Add edges for each line geometry and store attributes as edge properties
    for feature in features:
        if feature['geometry']['type'] == 'LineString':
            coordinates = feature['geometry']['coordinates']
            start = tuple(coordinates[0])
            end = tuple(coordinates[-1])
            G.add_edge(start, end, **feature['properties'])

    return G

# Example usage
G = graph_from_shapefile('path/to/shapefile.shp')
