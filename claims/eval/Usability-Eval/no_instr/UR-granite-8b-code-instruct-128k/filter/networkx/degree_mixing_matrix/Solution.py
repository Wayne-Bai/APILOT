import networkx as nx

def mixing_matrix(G):
    """
    Returns the mixing matrix for the attribute "community" of the given graph G.
    """
    matrix = nx.to_numpy_matrix(G, nodelist=sorted(G.nodes()))
    return matrix
