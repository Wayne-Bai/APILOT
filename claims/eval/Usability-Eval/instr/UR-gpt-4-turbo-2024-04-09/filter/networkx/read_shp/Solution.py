import networkx as nx
import geopandas as gpd
import os

def load_network_from_shapefile(shapefile_path):
    """ Loads a network graph from shapefiles, where points are nodes and lines are edges.
    
    Args:
    shapefile_path (str): Path to a shapefile or directory containing multiple shapefiles.

    Returns:
    networkx.DiGraph: The directed graph generated from the shapefiles.
    """
    G = nx.DiGraph()
    
    # Check if the path is a directory or a file
    if os.path.isdir(shapefile_path):
        # If directory, list all shapefiles
        files = [os.path.join(shapefile_path, f) for f in os.listdir(shapefile_path) if f.endswith('.shp')]
    else:
        # If single file
        files = [shapefile_path]
    
    for file in files:
        # Load each shapefile into a GeoDataFrame
        gdf = gpd.read_file(file)
        
        # Process each geometry in the file
        for idx, row in gdf.iterrows():
            geom_type = row.geometry.geom_type
            
            if geom_type == 'Point':
                # Create a node for each point
                node_key = tuple(row.geometry.coords[0])  # Assumes points
                G.add_node(node_key, **row)
            
            elif geom_type == 'LineString':
                # Create an edge for each line, use start and end points as keys
                start_node_key = tuple(row.geometry.coords[0])
                end_node_key = tuple(row.geometry.coords[-1])
                # Add attributes, simplifying the line to start and end coordinates
                attributes = row.to_dict()
                attributes.pop('geometry', None)  # Remove geometry from attributes, if required
                G.add_edge(start_node_key, end_node_key, **attributes)
    
    return G

# Usage example:
# graph = load_network_from_shapefile('/path/to/shapefile/or/directory')
