import numpy as np
from scipy.sparse import csr_matrix

def laplacian_matrix(adjacency):
    """
    Computes the Laplacian matrix of a directed graph.

    Parameters:
    adjacency (2D array-like): Adjacency matrix of the directed graph.

    Returns:
    scipy.sparse.csr_matrix: Laplacian matrix of the graph.
    """
    adjacency = csr_matrix(adjacency)
    out_degree = np.array(adjacency.sum(axis=1)).flatten()
    
    # Create the degree matrix as a diagonal matrix
    degree_matrix = csr_matrix(np.diag(out_degree))

    # Laplacian matrix = Degree matrix - Adjacency matrix
    laplacian = degree_matrix - adjacency

    return laplacian

# Example usage
adjacency_matrix = np.array([[0, 1, 1],
                              [0, 0, 1],
                              [1, 0, 0]])

laplacian = laplacian_matrix(adjacency_matrix)
print(laplacian.toarray())
