import scipy.sparse as sp
import numpy as np

def calculate_graph_laplacian(adjacency_matrix: sp.spmatrix) -> sp.spmatrix:
    degrees = np.array(adjacency_matrix.sum(axis=1))
    identity_matrix = np.eye(degrees.size)
    return identity_matrix - adjacency_matrix.tocsr() + adjacency_matrix

# Example usage:
adj_matrix = sp.csr_matrix([
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
])

laplacian = calculate_graph_laplacian(adj_matrix)
print(laplacian.toarray())
