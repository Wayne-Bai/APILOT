import numpy as np

def zero_below_diagonal(matrix, k):
    """
    Make a copy of a matrix with elements below the kth diagonal zeroed.

    Args:
        matrix (numpy.ndarray): Input matrix.
        k (int): Diagonal number.

    Returns:
        numpy.ndarray: Copy of the input matrix with elements below the kth diagonal zeroed.
    """
    # Create a copy of the input matrix to avoid modifying the original
    result = matrix.copy()

    # Calculate the rows and columns to zero
    rows, cols = result.shape
    for i in range(rows):
        for j in range(cols):
            if j - i > k:
                result[i, j] = 0

    return result

# Example usage:
matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
k = 1

result = zero_below_diagonal(matrix, k)
print(result)
