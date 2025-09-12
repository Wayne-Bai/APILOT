import os
import fiona
import networkx as nx
from shapely.geometry import shape, GeometryCollection

# Create a(logger=False) directed graph
# This graph will store the data from shapefiles

def load_shapefiles(directory=False, shapefile_path=False):
    """
    Reads a single shapefile or a directory containing many shapefiles
    and returns a networkx.DiGraph.

    Parameters:
    - directory (bool): Whether to read from a directory or a single shapefile
    - shapefile_path (str): The path to the shapefile (if directory is False)

    Returns:
    - g (DiGraph): A directed graph where point geometries are translated into nodes and lines into edges
    """
    g = nx.DiGraph()

    if directory:
        # Read all shapefiles from the given directory
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".shp"):
                    shp_path = os.path.join(root, file)
                    load_shapefile(g, shp_path)
    elif shapefile_path:
        load_shapefile(g, shapefile_path)
    else:
        raise ValueError("Either directory or shapefile_path must be provided")

    return g


def load_shapefile(g, shp_path):
    """
    Reads a single shapefile and adds its geometries to the graph.
    """
    with fiona.open(shp_path, 'r') as source:
        for feature in source:
            geometry = shape(feature['geometry'])
            if geometry.geom_type == 'Point':
                # Add point as node to the graph
                g.add_node((geometry.coords[0][0], geometry.coords[0][1]), **feature['properties'])
            elif geometry.geom_type in ['LineString', 'MultiLineString']:
                # Add line as edge to the graph, with start and end coordinates as keys
                coords = geometry.coords[:2]
                g.add_edge((coords[0][0], coords[0][1]), (coords[-1][0], coords[-1][1]), **feature['properties'])


# Example usage
directory = '/path/to/your/directory'
g = load_shapefiles(directory=directory)
print(g.nodes.data())  # print information about all nodes
print(g.edges.data())  # print information about all edges
