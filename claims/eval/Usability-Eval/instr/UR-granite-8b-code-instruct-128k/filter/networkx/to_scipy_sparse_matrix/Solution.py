import networkx as nx
def adjacency_matrix(graph):
    """Return the graph adjacency matrix as a SciPy sparse matrix."""
    return nx.to_scipy_sparse_matrix(graph)