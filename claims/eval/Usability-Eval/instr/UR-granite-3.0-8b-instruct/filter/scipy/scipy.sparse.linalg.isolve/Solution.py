import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve

# Assuming A and b are defined as follows:
# A is a sparse matrix in Compressed Sparse Column (CSC) format
# b is a vector or a matrix

# Convert b to a CSC matrix if it's a vector
if b.ndim == 1:
    b = csc_matrix(b)

# Solve the sparse linear system Ax=b
x = spsolve(A, b)
