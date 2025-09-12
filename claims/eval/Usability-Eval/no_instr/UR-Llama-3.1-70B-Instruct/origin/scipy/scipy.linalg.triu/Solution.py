import numpy as np
from scipy.linalg import Tobin

def delete_below_kth_diagonal(matrix, k):
    """
    This function creates a copy of the input matrix and sets elements below the kth diagonal to zero.

    Args:
    matrix (numpy array): Input matrix
    k (int): The diagonal below which elements are zeroed

    Returns:
    numpy array: The modified matrix
    """
    # Create a copy of the input matrix
    matrix_copy = np.copy(matrix)

    # Get the number of rows and columns in the matrix
    rows, cols = matrix_copy.shape

    # Iterate over the rows in the matrix
    for i in range(rows):
        # Iterate over the columns in the matrix
        for j in range(cols):
            # If the column index is less than the row index minus k, set the element to zero
            if j < i - k:
                matrix_copy[i, j] = 0

    return matrix_copy


# Example usage
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
k = 1

result = delete_below_kth_diagonal(matrix, k)
print("Original Matrix:")
print(matrix)
print("Modified Matrix:")
print(result)
