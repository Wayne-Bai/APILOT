import networkx as nx

def has_eulerian_path(G, source=None):
    if not nx.is_connected(G):
        return False
    if source is not None and source not in G:
        return False
    if not nx.is_bipartite(G):
        return False
    if source is None:
        source = nx.connected_component_most_nodes(G)
    return nx.is_semieulerian(G, source)
