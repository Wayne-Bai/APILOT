from scipy import sparse, linalg

# Define the sparse matrix A and the vector/matrix b
# For example, let's use a sparse matrix and a vector
A = sparse.csr_matrix([[1, 2, 0], [0, 1, 3], [4, 0, 5]])
b = np.array([1, 2, 3])

# Solve the sparse linear system Ax = b
x = linalg.solve(A, b)

print("Solution:", x)
