import networkx as nx
from shapely.geometry import LineString

def generate_edges(geom):
    edges = []
    for i in range(len(geom)):
        if i < len(geom) - 1:
            start_point = geom[i]
            end_point = geom[i + 1]
            edges.append((start_point.coords[0], end_point.coords[0]))
    return edges

def read_shp(file_path):
    G = nx.Graph()
    with open(file_path, 'r') as f:
        for line in f:
            geom = LineString(line.split(' ')[1:].split(','))
            edges = generate_edges(geom)
            G.add_edges_from(edges)
    return G
