import scipy.sparse
from scipy.sparse.linalg import spsolve

# Define the sparse matrix A and vector/matrix b
A = scipy.sparse.csr_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = [1, 2, 3]

# Solve the linear system Ax = b
x = spsolve(A, b)

print(f"Solution: {x}")
