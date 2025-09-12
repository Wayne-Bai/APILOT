
import networkx as nx

def has_eulerian_path(G, source=None):
    if source is not None:
        if nx.is_connected(G) and G.degree(source) % 2 == 1:
            return nx.is_eulerian(G)
        else:
            return False
    else:
        return nx.is_eulerian(G)
