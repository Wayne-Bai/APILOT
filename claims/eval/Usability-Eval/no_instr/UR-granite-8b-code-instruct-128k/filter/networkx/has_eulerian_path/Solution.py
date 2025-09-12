import networkx as nx

def has_eulerian_path(G, source=None):
    if source is None:
        return nx.has_eulerian_path(G)
    else:
        return nx.has_eulerian_path(G, source=source)
