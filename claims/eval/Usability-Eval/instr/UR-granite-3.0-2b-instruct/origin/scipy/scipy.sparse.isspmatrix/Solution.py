import numpy as np
from scipy.sparse import issparse

# Create a sparse matrix
sparse_matrix = np.array([[0, 0, 3], [4, 0, 0], [0, 5, 0]])

# Check if the matrix is sparse
if issparse(sparse_matrix):
    print("The matrix is sparse.")
else:
    print("The matrix is not sparse.")
