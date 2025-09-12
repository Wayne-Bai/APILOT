import networkx as nx

def create_graph_from_sparse_matrix(adj_matrix):
    G = nx.from_numpy_array(adj_matrix)
    return G
