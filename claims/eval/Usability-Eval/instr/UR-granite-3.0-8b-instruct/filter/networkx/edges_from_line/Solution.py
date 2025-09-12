import networkx as nx
from shapely.geometry import LineString

def read_shp(file_path):
    G = nx.Graph()
    with open(file_path, 'r') as file:
        for line in file:
            geom = LineString(line.split())  # Assuming the shapefile is in WKT format
            G.add_edge(geom.coords[0], geom.coords[-1], weight=geom.length)  # Add edge with weight as length
    return G
