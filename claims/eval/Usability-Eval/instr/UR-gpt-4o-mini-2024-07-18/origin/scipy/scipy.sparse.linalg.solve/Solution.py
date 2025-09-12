import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve

def solve_sparse_linear_system(A, b):
    # Convert matrix A to a compressed sparse column format if it's not already
    A_csc = csc_matrix(A)
    
    # Use spsolve to solve for x in Ax = b
    x = spsolve(A_csc, b)
    
    return x

# Example usage:
# A is a sparse matrix (numpy array or another format that can be converted)
A = np.array([[3, 2, 0], [0, 0, 1], [1, 0, 3]])
b = np.array([2, 1, 4])

result = solve_sparse_linear_system(A, b)
print(result)
