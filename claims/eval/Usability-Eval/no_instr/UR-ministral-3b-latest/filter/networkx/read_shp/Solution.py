import os
import sys
import geopandas as gpd
import networkx as nx
from shapely.geometry import Point, LineString
from scipy.spatial import distance
import math

# Function to generate a NetworkX DiGraph from shapefiles
def generate_graph_from_shapefile(shapefile_path):
    # Read the shapefile
    gdf = gpd.read_file(shapefile_path)

    # Initialize the DiGraph
    graph = nx.DiGraph()

    # Add points to nodes
    for i, row in gdf.iterrows():
        geometry = row['geometry']
        if isinstance(geometry, Point):
            node = (geometry.x, geometry.y)
            graph.add_node(node)

    # Add lines to edges
    for i, row in gdf.iterrows():
        geometry = row['geometry']
        if isinstance(geometry, LineString):
            start_point = (geometry.bounds[0], geometry.bounds[1])
            end_point = (geometry.bounds[2], geometry.bounds[3])
            graph.add_edge(start_point, end_point)

    return graph

# Example usage
if __name__ == '__main__':
    shapefile_path = 'path/to/shapefile.shp'
    graph = generate_graph_from_shapefile(shapefile_path)
    print(f"Graph created with {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges.")
