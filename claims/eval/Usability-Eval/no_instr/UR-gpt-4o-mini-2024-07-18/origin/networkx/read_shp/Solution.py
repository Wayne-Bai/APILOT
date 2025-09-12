import networkx as nx
import geopandas as gpd
import os

def shapefiles_to_digraph(shapefile_or_directory):
    # Initialize a directed graph
    G = nx.DiGraph()

    # Check if the input is a directory or a single shapefile
    if os.path.isdir(shapefile_or_directory):
        shapefiles = [os.path.join(shapefile_or_directory, f) for f in os.listdir(shapefile_or_directory) if f.endswith('.shp')]
    else:
        shapefiles = [shapefile_or_directory]

    for shapefile in shapefiles:
        # Read the shapefile using geopandas
        gdf = gpd.read_file(shapefile)
        
        # Process point geometries to create nodes
        if 'geometry' in gdf:
            for idx, row in gdf.iterrows():
                if row['geometry'].geom_type == 'Point':
                    G.add_node(tuple(row['geometry'].coords[0]), **row.drop('geometry').to_dict())
                elif row['geometry'].geom_type in ['LineString', 'MultiLineString']:
                    # Simplify line geometries into start and end coordinates
                    if row['geometry'].geom_type == 'LineString':
                        points = [tuple(coord) for coord in row['geometry'].coords]
                        start = points[0]
                        end = points[-1]
                        G.add_edge(start, end, **row.drop('geometry').to_dict())
                    elif row['geometry'].geom_type == 'MultiLineString':
                        for line in row['geometry']:
                            points = [tuple(coord) for coord in line.coords]
                            start = points[0]
                            end = points[-1]
                            G.add_edge(start, end, **row.drop('geometry').to_dict())
    
    return G
