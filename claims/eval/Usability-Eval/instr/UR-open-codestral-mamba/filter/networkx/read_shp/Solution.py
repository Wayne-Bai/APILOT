import os
import networkx as nx
import geopandas as gpd
from shapely.geometry import LineString

def shape_file_to_di_graph(file_path):
    di_graph = nx.MultiDiGraph()

    # Read shapefile
    gdf = gpd.read_file(file_path)

    for _, row in gdf.iterrows():
        # Convert geometries to coordinate tuples
        geom = row['geometry']
        if isinstance(geom, LineString):
            coords = [geom.coords[0], geom.coords[-1]]
            for i in range(len(coords) - 1):
                start = coords[i]
                end = coords[i + 1]
                di_graph.add_edge(start, end, attr_dict=row.drop('geometry').to_dict())
        else:
            for point in geom:
                di_graph.add_node(tuple(point), attr_dict=row.drop('geometry').to_dict())

    return di_graph

def shapefile_or_directory_to_di_graph(path):
    di_graph = nx.MultiDiGraph()

    if os.path.isfile(path):
        di_graph = merge_di_graphs(di_graph, shape_file_to_di_graph(path))
    else:
        for root, dir, files in os.walk(path):
            for file in files:
                if file.endswith('.shp'):
                    cur_di_graph = shape_file_to_di_graph(os.path.join(root, file))
                    di_graph = merge_di_graphs(di_graph, cur_di_graph)

    return di_graph
