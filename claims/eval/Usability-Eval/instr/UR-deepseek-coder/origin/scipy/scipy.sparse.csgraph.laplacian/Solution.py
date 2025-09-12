import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import inv

def laplacian_of_directed_graph(adj_matrix):
    """
    Compute the Laplacian matrix of a directed graph.

    Parameters:
    adj_matrix (numpy.ndarray): The adjacency matrix of the directed graph.

    Returns:
    numpy.ndarray: The Laplacian matrix of the directed graph.
    """
    # Compute the out-degree matrix
    out_degree_matrix = np.diag(np.sum(adj_matrix, axis=1))
    
    # Compute the Laplacian matrix
    laplacian = out_degree_matrix - adj_matrix
    
    return laplacian

# Example usage:
# Define a directed graph adjacency matrix
adj_matrix = np.array([[0, 1, 0],
                       [0, 0, 1],
                       [1, 0, 0]])

# Compute the Laplacian matrix
laplacian_matrix = laplacian_of_directed_graph(adj_matrix)
print(laplacian_matrix)
