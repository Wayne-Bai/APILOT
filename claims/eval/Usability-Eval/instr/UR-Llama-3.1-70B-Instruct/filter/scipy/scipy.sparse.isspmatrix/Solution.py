import scipy.sparse as sparse
import numpy as np

# Function to check if a matrix is sparse
def is_sparse(matrix):
    return sparse.isspmatrix(matrix)

# Example usage:
# Create a sparse matrix
sparse_matrix = sparse.csr_matrix(np.array([[0, 1, 0], [0, 0, 2], [0, 0, 0]]))

# Check if the matrix is sparse
print(is_sparse(sparse_matrix))  # Output: True

# Create a non-sparse matrix
non_sparse_matrix = np.array([[0, 1, 0], [0, 0, 2], [0, 0, 0]])

# Check if the matrix is sparse
print(is_sparse(non_sparse_matrix))  # Output: False
