import scipy as sp

# Define the matrix A and the vector/matrix b
A = sp.sparse.csr_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = sp.sparse.csc_matrix([[1], [2], [3]])

# Solve the sparse linear system Ax=b
x = sp.sparse.linalg.spsolve(A, b)

print(x)
