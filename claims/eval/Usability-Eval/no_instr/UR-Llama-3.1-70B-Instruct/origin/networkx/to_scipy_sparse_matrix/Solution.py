import networkx as nx
from scipy import sparse

def adjacency_matrix(G):
    """
    Returns the graph adjacency matrix as a SciPy sparse matrix.

    Parameters
    ----------
    G : networkx.Graph
        The input graph.

    Returns
    -------
    A : scipy.sparse.csr.csr_matrix
        The adjacency matrix of the graph.
    """
    return nx.to_scipy_sparse_matrix(G, format='csr')

# Usage
if __name__ == "__main__":
    # Create an example graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 1)])

    # Get the adjacency matrix
    A = adjacency_matrix(G)

    # Print the adjacency matrix
    print(A.toarray())
