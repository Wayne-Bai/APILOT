import numpy as np
from scipy.sparse import csr_matrix

def laplacian_matrix(directed_graph):
    """
    Compute the Laplacian matrix of a directed graph.
    
    Parameters:
    directed_graph (np.ndarray): Adjacency matrix of the directed graph.
    
    Returns:
    np.ndarray: Laplacian matrix of the directed graph.
    """
    # Degree matrix
    degrees = np.sum(directed_graph, axis=1)
    degree_matrix = np.diag(degrees)

    # Laplacian matrix
    laplacian = degree_matrix - directed_graph
    
    return laplacian

# Example usage
if __name__ == "__main__":
    # Example directed graph as an adjacency matrix
    adj_matrix = np.array([[0, 1, 0],
                           [0, 0, 1],
                           [1, 0, 0]])
    
    laplacian = laplacian_matrix(adj_matrix)
    print("Laplacian matrix:\n", laplacian)
