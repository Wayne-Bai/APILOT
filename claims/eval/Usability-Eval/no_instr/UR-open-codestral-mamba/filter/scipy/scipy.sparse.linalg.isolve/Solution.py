import scipy.sparse.linalg

def solve_sparse_linear_system(A, b):
    # Solve the sparse linear system Ax=b
    x = scipy.sparse.linalg.spsolve(A, b)
    return x
