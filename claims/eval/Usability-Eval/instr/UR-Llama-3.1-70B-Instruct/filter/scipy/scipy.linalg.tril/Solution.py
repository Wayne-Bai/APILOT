import numpy as np
from scipy import ndimage

def zero_above_diagonal(matrix, k):
    """
    Make a copy of a matrix with elements above the kth diagonal zeroed.

    Parameters:
    matrix (numpy.ndarray): Input matrix
    k (int): Diagonal index

    Returns:
    numpy.ndarray: Matrix copy with elements above the kth diagonal zeroed
    """
    # Get matrix dimensions
    rows, cols = matrix.shape
    
    # Create a copy of the matrix
    result = matrix.copy()
    
    # Zero elements above the kth diagonal
    result[np.arange(rows)[:, None] + k < np.arange(cols)] = 0
    
    return result

# Example usage:
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

k = 1

result = zero_above_diagonal(matrix, k)
print("Original matrix:")
print(matrix)
print("\nMatrix copy with elements above the {}th diagonal zeroed:".format(k))
print(result)
