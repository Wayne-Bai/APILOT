from scipy.sparse.linalg import spsolve

# Assuming A and b are defined as sparse matrices
# A = ...
# b = ...

# Solve the sparse linear system Ax=b
x = spsolve(A, b)
