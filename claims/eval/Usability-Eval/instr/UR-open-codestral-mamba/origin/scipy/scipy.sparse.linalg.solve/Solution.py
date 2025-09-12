import scipy
from scipy import sparse
from scipy.sparse.linalg import spsolve

# Define the sparse matrix A
A = sparse.csr_matrix([[1, 0, 2], [0, 0, 3], [4, 0, 5]])

# Define the matrix b
b = [[1,2],[3,4],[5,6]]

# Solve the system
x = spsolve(A, b)

# Print the solution
print(x)
