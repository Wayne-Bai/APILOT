import scipy.sparse as sp

def is_sparse_matrix(x):
    return sp.issparse(x)

# Example usage
matrix = sp.csr_matrix([[0, 0, 1], [0, 0, 0], [3, 0, 0]])
print(is_sparse_matrix(matrix))  # Output: True

dense_matrix = [[1, 2, 3], [4, 5, 6]]
print(is_sparse_matrix(dense_matrix))  # Output: False
