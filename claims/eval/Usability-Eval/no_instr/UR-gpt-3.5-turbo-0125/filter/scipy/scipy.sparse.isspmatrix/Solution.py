
import scipy.sparse

def is_sparse_matrix(x):
    return scipy.sparse.issparse(x)

# Example usage:
# matrix = scipy.sparse.csr_matrix([[1, 0, 0], [0, 0, 1]])
# print(is_sparse_matrix(matrix))
