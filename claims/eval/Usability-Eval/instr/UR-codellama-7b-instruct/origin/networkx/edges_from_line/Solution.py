import networkx as nx

def generate_edges(geom):
    edges = []
    for line in geom.get_lines():
        edges.append((line[0], line[1]))
    return edges
