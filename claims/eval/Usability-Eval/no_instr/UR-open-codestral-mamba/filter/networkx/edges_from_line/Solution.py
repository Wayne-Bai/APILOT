import networkx as nx

def generate_edges(geom):
    G = nx.Graph()
    for i in range(len(geom) - 1):
        # Add an edge between the current point and the next point in the line
        G.add_edge(geom[i], geom[i + 1])
    return G
