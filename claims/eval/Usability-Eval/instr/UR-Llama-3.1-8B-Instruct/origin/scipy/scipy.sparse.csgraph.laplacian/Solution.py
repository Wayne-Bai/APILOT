import numpy as np
from scipy.sparse import diags, coo_matrix
from scipy.linalg import solve
from scipy.sparse.linalg import spsolve

def laplacian_matrix(adjacency_matrix):
    """
    Compute the Laplacian matrix of a directed graph.

    Parameters:
    adjacency_matrix (numpy array): The adjacency matrix of the graph.

    Returns:
    laplacian_matrix (numpy array): The Laplacian matrix of the graph.
    """
    # Calculate the degrees of each node
    degrees = np.sum(adjacency_matrix, axis=1)

    # Compute the Laplacian matrix
    laplacian_diags = diags(degrees)
    laplacian_coo = coo_matrix(laplacian_diags.toarray())
    laplacian_coo.data = -laplacian_coo.data

    # Add the adjacency matrix to the coo matrix
    adjacency_coo = coo_matrix(adjacency_matrix)
    laplacian_coo = adjacency_coo + laplacian_coo

    # Convert back to a csr matrix for efficient computation
    laplacian_matrix = laplacian_coo.tocsr()
    
    return laplacian_matrix

# Example usage
adjacency_matrix = np.array([[0, 1, 0], [0, 0, 2], [3, 0, 0]])
laplacian = laplacian_matrix(adjacency_matrix)
print(laplacian.toarray())
