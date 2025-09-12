import networkx as nx
import scipy as sp
import numpy as np

def get_adjacency_matrix(G):
    """
    Return the graph adjacency matrix as a SciPy sparse matrix.

    Parameters
    ----------
    G : graph
       A NetworkX graph.

    Returns
    -------
    A : SciPy sparse matrix
       Adjacency matrix in CSR format.

    """
    return sp.sparse.csr_matrix(nx.adj_matrix(G))

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4)])
G.add_nodes_from([1, 2, 3, 4])

adj_matrix = get_adjacency_matrix(G)
print(adj_matrix.toarray())
