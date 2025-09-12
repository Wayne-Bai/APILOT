import networkx as nx

# Return the graph adjacency matrix as a SciPy sparse matrix.
def get_adjacency_matrix(graph):
    return nx.to_scipy_sparse_matrix(graph)
