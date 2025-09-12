import networkx as nx
import os
import geopandas as gpd

def read_shapefile_to_graph(shapefile_path):
    """
    Reads a shapefile or a directory of shapefiles and generates a directed graph.
    Nodes represent points with coordinates as keys. Edges represent line geometries simplified into start and end coordinates.
    
    Args:
    shapefile_path (str): Path to the shapefile or a directory containing multiple shapefiles
    
    Returns:
    nx.DiGraph: A directed graph with nodes and edges from shapefiles
    """
    G = nx.DiGraph()
    
    # Check if the input is a directory or a single file
    if os.path.isdir(shapefile_path):
        # List all shapefiles in the directory
        shapefiles = [os.path.join(shapefile_path, f) for f in os.listdir(shapefile_path) if f.endswith('.shp')]
    else:
        shapefiles = [shapefile_path]
    
    for shp in shapefiles:
        # Load the shapefile
        gdf = gpd.read_file(shp)
        
        # Iterate through the Geodataframe to create nodes and edges
        for idx, row in gdf.iterrows():
            geom_type = row.geometry.geom_type
            
            if geom_type == 'Point':
                # Add point as node
                point = row.geometry
                G.add_node((point.x, point.y), **row)
                
            elif geom_type in ['LineString', 'MultiLineString']:
                if geom_type == 'MultiLineString':
                    # Simplify MultiLineString to LineString (taking the first line)
                    line = row.geometry[0]
                else:
                    line = row.geometry
                
                start_coord = (line.coords[0][0], line.coords[0][1])
                end_coord = (line.coords[-1][0], line.coords[-1][1])
                
                # Add nodes for start and end points
                if start_coord not in G:
                    G.add_node(start_coord)
                if end_coord not in G:
                    G.add_node(end_coord)
                
                # Add edge from start to end point
                G.add_edge(start_coord, end_coord, **row)
    
    return G
