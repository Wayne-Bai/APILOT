from scipy import sparse, linalg

# Define the sparse matrix A and the vector b
# Here, we assume that A and b are already defined

# Solve the sparse linear system Ax = b
x = linalg.sparse.spsolve(A, b)
