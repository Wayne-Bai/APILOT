
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve

# Define the coefficient matrix A and the dependent variable vector b
A = csc_matrix([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]])
b = np.array([1, -2, 0])

# Solve the sparse linear system Ax=b
x = spsolve(A, b)

# Print the solution vector x
print(x)
