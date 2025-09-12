import numpy as np
from scipy.linalg import tril

def zero_above_kth_diag(matrix, k):
    """
    Create a copy of the matrix with elements above the k-th diagonal zeroed.

    Parameters:
    matrix (ndarray): Input matrix.
    k (int): The index of the diagonal above which elements are zeroed.
             k = 0 is the main diagonal,
             k > 0 is above the main diagonal.

    Returns:
    ndarray: Matrix with specified elements zeroed.
    """
    # Use tril to get the lower triangular matrix with respect to the k-th diagonal
    return tril(matrix, k=k)

# Example Usage:
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])

k = 1
result = zero_above_kth_diag(matrix, k)
print(result)
