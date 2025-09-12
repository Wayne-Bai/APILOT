
import numpy as np
from scipy.sparse import issparse

# create a sample sparse matrix
matrix = np.random.rand(100, 100)
matrix[np.triu_indices(100)] = 0

# check if the matrix is sparse using the issparse function
if issparse(matrix):
    print("The matrix is sparse")
else:
    print("The matrix is not sparse")
