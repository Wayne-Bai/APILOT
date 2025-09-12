import numpy as np
from scipy.sparse import issparse

# Create a random sparse matrix
n = 100
density = 0.1
A = np.random.rand(n, n) * density
A[np.abs(A) < 0.5] = 0

# Use the issparse function to check if A is sparse
if issparse(A):
    print("The matrix is sparse")
else:
    print("The matrix is not sparse")
