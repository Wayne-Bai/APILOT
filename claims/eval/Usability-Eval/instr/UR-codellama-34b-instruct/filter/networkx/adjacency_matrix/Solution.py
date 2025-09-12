import networkx as nx

def get_adjacency_matrix(G):
    return nx.to_numpy_array(G)
