import networkx as nx

def has_eulerian_path(G, source=None):
    if source is not None:
        if G.degree(source) != 0:
            return False
        G = G.subgraph([source] + list(G.neighbors(source)))

    if not nx.is_connected(G):
        return False

    degree = G.degree()
    even_degree_nodes = [n for n, d in degree if d % 2 == 0]
    odd_degree_nodes = [n for n, d in degree if d % 2 != 0]

    if len(even_degree_nodes) == 0 and len(odd_degree_nodes) == 0:
        return True
    elif len(even_degree_nodes) == 0 or len(odd_degree_nodes) == 0:
        return False
    else:
        return len(odd_degree_nodes) == 2
