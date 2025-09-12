import scipy.sparse as sp
from scipy.sparse.linalg import spsolve

def solve_sparse_linear_system(A, b):
    """
    Solve the sparse linear system Ax = b, where A is a sparse matrix and b may be a vector or a matrix.
    
    Parameters:
    A (scipy.sparse matrix): The sparse matrix A.
    b (array-like): The vector or matrix b.

    Returns:
    x (array or matrix): The solution vector or matrix x.
    """
    
    # Check if b is a 2D array (matrix)
    if sp.issparse(b):
        # If b is sparse, convert to dense format for processing
        b = b.toarray()
        
    # If b is a 1D array (vector), solve it directly
    if b.ndim == 1:
        x = spsolve(A, b)
    else:
        # If b is a 2D array (matrix), solve for each column separately
        x = np.empty_like(b)
        for i in range(b.shape[1]):
            x[:, i] = spsolve(A, b[:, i])
    
    return x
