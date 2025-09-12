# Importing the necessary libraries
import numpy as np
from scipy import sparse

# Creating a sparse matrix
A = sparse.csr_matrix([[0, 2, 0], [0, 0, 3], [4, 0, 5]])

# Checking if the matrix is of type numpy.ndarray
def is_sparse_matrix(x):
    return isinstance(x, sparse.spmatrix)

# Printing the result
print(is_sparse_matrix(A))  # This should print: True
print(is_sparse_matrix(np.array([[1, 2], [3, 4]])))  # This should print: False
