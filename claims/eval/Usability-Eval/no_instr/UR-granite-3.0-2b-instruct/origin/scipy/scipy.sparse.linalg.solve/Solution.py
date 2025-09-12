from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve

# Define the sparse matrix A and the vector b
# For example, let's use a 3x3 sparse matrix and a 3x1 vector
A = csr_matrix([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
b = np.array([4, 5, 6])

# Solve the linear system Ax = b
x = spsolve(A, b)

print("The solution is:", x)
