
import numpy as np
from scipy.sparse.linalg import spsolve

# Create your sparse matrix A and vector/matrix b
A = YOUR_SPARSE_MATRIX
b = YOUR_VECTOR_OR_MATRIX

# Solve the sparse linear system Ax=b
x = spsolve(A, b)

print(x)
