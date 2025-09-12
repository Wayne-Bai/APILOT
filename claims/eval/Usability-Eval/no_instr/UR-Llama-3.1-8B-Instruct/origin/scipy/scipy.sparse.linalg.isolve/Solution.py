# Import necessary libraries from scipy
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve
import numpy as np

# Define a function to solve the sparse linear system Ax=b
def solve_sparse_linear_system(A, b):
    """
    Solves the sparse linear system Ax=b, where b may be a vector or a matrix.

    Parameters:
    A (sparse matrix): The sparse matrix for which the linear system will be solved
    b (numpy array): The right-hand side vector or matrix of the linear system

    Returns:
    x (numpy array): The solution vector or matrix of the linear system Ax=b
    """
    
    # Convert input matrix A to a csr_matrix
    A_csr = csr_matrix(A)
    
    # Check if b is a vector or a matrix
    if isinstance(b, np.ndarray) and b.ndim == 1:
        # If b is a vector, solve the linear system using spsolve
        b_array = b
    else:
        # If b is a matrix, solve each column of the linear system
        b_array = np.array(np.hsplit(b, b.shape[1]))
    
    # Solve the linear systems
    x = []
    for b_col in b_array:
        sol = spsolve(A_csr, b_col)
        x.append(sol)
    
    # If b was a vector, return a vector
    if isinstance(b, np.ndarray) and b.ndim == 1:
        return np.array(x).squeeze()
    else:
        # If b was a matrix, return a matrix
        return np.array(x).T

# Example usage
if __name__ == "__main__":
    # Define a sparse matrix A
    A = np.array([[3, 1], [1, 4]])
    
    # Define a vector b
    b = np.array([9, 12])
    
    # Define a matrix b
    b_matrix = np.array([[9, 12], [15, 20]])
    
    print("Solution for vector b:")
    print(solve_sparse_linear_system(A, b))
    
    print("\nSolutions for matrix b:")
    print(solve_sparse_linear_system(A, b_matrix))
