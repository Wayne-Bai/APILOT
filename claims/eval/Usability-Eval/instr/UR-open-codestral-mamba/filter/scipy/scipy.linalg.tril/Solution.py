import numpy as np
from scipy import sparse

def zero_above_kth_diagonal(matrix, k):
    # Convert numpy matrix to sparse CSR matrix for efficiency
    sparse_matrix = sparse.csr_matrix(matrix)

    # Create a triangular mask where the above kth diagonal is True
    mask = sparse.triu(sparse_matrix, k + 1)

    # Perform elementwise multiplication to set above-kth diagonal elements to zero
    result = sparse.csr_matrix(sparse_matrix.multiply(mask))

    return result.toarray()

# Test the function
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

k = 1
zeroed_matrix = zero_above_kth_diagonal(matrix, k)
print(zeroed_matrix)
