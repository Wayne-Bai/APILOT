import scipy.sparse

def is_sparse_matrix(x):
    return isinstance(x, scipy.sparse.spmatrix)

# Example usage:
matrix = scipy.sparse.csr_matrix([[1, 0], [0, 2]])
print(is_sparse_matrix(matrix))  # Output: True

density_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(is_sparse_matrix(density_matrix))  # Output: False
