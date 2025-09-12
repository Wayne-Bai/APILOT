import networkx as nx
from shapely.geometry import LineString

def generate_edges(geom):
    edges = []
    for i in range(len(geom) - 1):
        line1 = LineString(geom[i].coords)
        line2 = LineString(geom[i + 1].coords)
        if line1.intersects(line2):
            edges.append((i, i + 1))
    return edges

def read_shp(file_path):
    G = nx.Graph()
    with open(file_path, 'r') as f:
        for line in f:
            geom = LineString(line.split(' ')[1:].split(','))
            edges = generate_edges(geom)
            for u, v in edges:
                G.add_edge(u, v)
    return G
