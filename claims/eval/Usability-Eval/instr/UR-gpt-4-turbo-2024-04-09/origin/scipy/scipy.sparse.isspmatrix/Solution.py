import scipy.sparse

def is_sparse_matrix(x):
    return scipy.sparse.issparse(x)

# Example usage:
# Create a sparse matrix for demonstration
sparse_matrix = scipy.sparse.csr_matrix([[1, 0, 0], [0, 0, 0], [0, 0, 1]])

# Check if the matrix is sparse
print(is_sparse_matrix(sparse_matrix))  # Output: True

# Check with regular list
print(is_sparse_matrix([[1, 0, 0], [0, 0, 0], [0, 0, 1]]))  # Output: False
