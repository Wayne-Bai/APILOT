from scipy.sparse import issparse

def is_sparse_matrix(x):
    return issparse(x)

# Example usage:
# from scipy.sparse import csr_matrix
# matrix = csr_matrix([[0, 0], [1, 0]])
# print(is_sparse_matrix(matrix))  # Output: True
