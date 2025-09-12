from scipy.sparse.linalg import spsolve

# Assuming A is a scipy sparse matrix and b is a vector or a matrix
# Solve the sparse linear system Ax=b

# If b is a vector
x = spsolve(A, b)

# If b is a matrix
x = spsolve(A, b)
