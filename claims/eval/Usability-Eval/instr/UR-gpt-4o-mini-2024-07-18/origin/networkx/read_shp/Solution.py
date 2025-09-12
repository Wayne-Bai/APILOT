import networkx as nx
import geopandas as gpd
import os

def shapefile_to_digraph(shapefile):
    gdf = gpd.read_file(shapefile)
    
    # Create a directed graph
    G = nx.DiGraph()

    # Process point geometries and add them as nodes
    points = gdf[gdf.geometry.geom_type == 'Point']
    for idx, point in points.iterrows():
        G.add_node(tuple(point.geometry.coords[0]), **point.drop('geometry').to_dict())

    # Process line geometries and add them as edges
    lines = gdf[gdf.geometry.geom_type == 'LineString']
    for idx, line in lines.iterrows():
        coords = list(line.geometry.coords)
        start = tuple(coords[0])
        end = tuple(coords[-1])
        G.add_edge(start, end, **line.drop('geometry').to_dict())

    return G

def directory_to_digraph(directory):
    G = nx.DiGraph()
    
    for filename in os.listdir(directory):
        if filename.endswith('.shp'):
            filepath = os.path.join(directory, filename)
            G_sub = shapefile_to_digraph(filepath)
            G = nx.compose(G, G_sub)

    return G
