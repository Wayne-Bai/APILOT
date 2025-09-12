import networkx as nx

def generate_edges(geom):
    G = nx.Graph()
    for line in geom:
        start_point = line.coords[0]
        end_point = line.coords[-1]
        G.add_edge(start_point, end_point)
    return G
