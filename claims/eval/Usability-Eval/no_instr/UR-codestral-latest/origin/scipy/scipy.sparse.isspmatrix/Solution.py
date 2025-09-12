import scipy.sparse as sp
import numpy as np

def is_sparse(x):
    return isinstance(x, sp.sparse.spmatrix)

# Example usage:
matrix = np.array([[1, 0, 0], [0, 0, 2], [0, 0, 0]])
sparse_matrix = sp.csr_matrix(matrix)

print(is_sparse(matrix))  # False
print(is_sparse(sparse_matrix))  # True
