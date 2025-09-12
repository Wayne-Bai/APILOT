import numpy as np
from scipy.sparse import csgraph
from scipy.sparse import csr_matrix

def laplacian_directed_graph(adjacency_matrix):
    """
    Compute the Laplacian of a directed graph given its adjacency matrix.

    Parameters:
    adjacency_matrix (numpy.ndarray): A square adjacency matrix of the graph

    Returns:
    numpy.ndarray: Laplacian matrix of the directed graph
    """
    # Ensure the adjacency matrix is in the correct sparse matrix format
    adjacency_matrix = csr_matrix(adjacency_matrix)
    
    # Compute the Laplacian matrix using the sparse graph utilities in scipy
    laplacian_matrix = csgraph.laplacian(adjacency_matrix, normed=False)

    return laplacian_matrix.toarray()

# Example usage:
if __name__ == "__main__":
    # Example adjacency matrix for a directed graph
    adj_matrix = np.array([
        [0, 1, 1],
        [0, 0, 1],
        [0, 1, 0]
    ])
    
    laplacian = laplacian_directed_graph(adj_matrix)
    print("Laplacian matrix of the directed graph:\n", laplacian)
