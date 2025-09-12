import scipy.sparse

def is_sparse_matrix(x):
    return scipy.sparse.issparse(x)

# Example usage
from scipy.sparse import csr_matrix

sparse_matrix = csr_matrix([[0, 0, 3], [4, 0, 0], [0, 0, 0]])
dense_matrix = [[1, 2, 3], [4, 5, 6]]

print(is_sparse_matrix(sparse_matrix))  # Output: True
print(is_sparse_matrix(dense_matrix))    # Output: False
