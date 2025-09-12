import networkx as nx

def to_scipy_sparse_matrix(G):
    """Return the graph adjacency matrix as a SciPy sparse matrix.

    Parameters
    ----------
    G : NetworkX graph

    Returns
    -------
    adj_matrix : scipy.sparse.csr.csr_matrix
        The adjacency matrix of the graph as a SciPy sparse matrix.

    """
    import scipy.sparse
    return scipy.sparse.csr_matrix(nx.adj_matrix(G))
