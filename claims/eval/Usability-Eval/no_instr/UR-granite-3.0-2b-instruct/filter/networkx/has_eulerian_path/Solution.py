import networkx as nx

def has_eulerian_path(G, source=None):
    if not nx.is_connected(G):
        return False

    if source is not None:
        return nx.has_path(G, source, source)

    return nx.has_path(G, 0, len(G) - 1)
