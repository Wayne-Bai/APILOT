import networkx as nx

def generate_edges(geom):
    G = nx.Graph()
    for i, line in enumerate(geom):
        G.add_edge(i, i+1, {'geometry': line})
    return G
