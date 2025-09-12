import numpy as np
from scipy.sparse import lil_matrix, csr_matrix

def laplacian_of_directed_graph(adj_matrix):
    n = adj_matrix.shape[0]

    # Create a zeros matrix of size (n, n)
    laplacian = lil_matrix((n, n), dtype=np.uint8)

    # Populate the Laplacian matrix
    rows, cols = adj_matrix.nonzero()
    for i in range(len(rows)):
        laplacian[rows[i], cols[i]] = 1

    # Diagonal entries
    diagonal = np.zeros(n, dtype=np.uint8)
    np.fill_diagonal(diagonal, 2)
    laplacian += diag(diagonal)

    # Convert to CSR matrix for efficient computation
    laplacian = csr_matrix(laplacian)

    return laplacian

# Example usage
if __name__ == "__main__":
    # Example adjacency matrix for a directed graph
    adj_matrix = np.array([
        [0, 1, 0],
        [0, 1, 0],
        [1, 0, 0]
    ], dtype=np.uint8)

    laplacian = laplacian_of_directed_graph(adj_matrix)
    print("Laplacian of directed graph:\n", laplacian.toarray())
