
import os
import geopandas as gpd
import networkx as nx

def create_digraph_from_shapefiles(shapefile_path):
    G = nx.DiGraph()
    
    def add_edge(geom, attributes):
        coords = list(geom.coords)
        start_node = coords[0]
        end_node = coords[-1]
        G.add_edge(start_node, end_node, **attributes)
    
    if os.path.isdir(shapefile_path):
        for filename in os.listdir(shapefile_path):
            if filename.endswith('.shp'):
                file_path = os.path.join(shapefile_path, filename)
                df = gpd.read_file(file_path)
                for idx, row in df.iterrows():
                    if row.geometry.geom_type == 'Point':
                        G.add_node((row.geometry.x, row.geometry.y), **row.drop('geometry').to_dict())
                    elif row.geometry.geom_type == 'LineString':
                        add_edge(row.geometry, row.drop('geometry').to_dict())
    elif os.path.isfile(shapefile_path):
        df = gpd.read_file(shapefile_path)
        for idx, row in df.iterrows():
            if row.geometry.geom_type == 'Point':
                G.add_node((row.geometry.x, row.geometry.y), **row.drop('geometry').to_dict())
            elif row.geometry.geom_type == 'LineString':
                add_edge(row.geometry, row.drop('geometry').to_dict())
    
    return G

# Example usage:
shapefile_path = 'path_to_shapefile_or_directory'
G = create_digraph_from_shapefiles(shapefile_path)
