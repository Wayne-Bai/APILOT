import networkx as nx
import geopandas as gpd
from shapely.geometry import Point, LineString

def shapefile_to_digraph(shapefile_path):
    # Load the shapefile using geopandas
    gdf = gpd.read_file(shapefile_path)
    
    # Initialize an empty directed graph
    G = nx.DiGraph()
    
    # Iterate over each row in the GeoDataFrame
    for idx, row in gdf.iterrows():
        geometry = row.geometry
        
        if isinstance(geometry, Point):
            # If the geometry is a Point, add it as a node
            G.add_node(geometry.coords[0], **row.drop('geometry').to_dict())
        
        elif isinstance(geometry, LineString):
            # If the geometry is a LineString, add it as an edge
            start_coords = geometry.coords[0]
            end_coords = geometry.coords[-1]
            G.add_edge(start_coords, end_coords, **row.drop('geometry').to_dict())
    
    return G

def process_shapefiles(directory_path):
    import os
    G = nx.DiGraph()
    
    # Iterate over all shapefiles in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".shp"):
            shapefile_path = os.path.join(directory_path, filename)
            G_sub = shapefile_to_digraph(shapefile_path)
            G = nx.compose(G, G_sub)
    
    return G

# Example usage:
# G = process_shapefiles('path/to/shapefiles')
