import scipy.sparse as sparse
import numpy as np

# Define the matrix A and the vector b
A = sparse.random(1000, 1000, density=0.01)
b = np.random.rand(1000)

# Solve the linear system Ax=b
x = sparse.linalg.spsolve(A, b)

# Print the solution
print(x)
