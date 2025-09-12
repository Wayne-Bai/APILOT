import networkx as nx

def adjacency_matrix(graph):
    adj_matrix = nx.to_scipy_sparse_matrix(graph)
    return adj_matrix
