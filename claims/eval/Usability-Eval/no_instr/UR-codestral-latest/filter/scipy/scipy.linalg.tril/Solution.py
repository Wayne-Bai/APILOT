import numpy as np

def zero_above_kth_diagonal(matrix, k):
    """
    Zero out the elements above the kth diagonal of a square matrix.

    Parameters:
    matrix (np.array): The input square matrix.
    k (int): The diagonal above which elements should be zeroed.

    Returns:
    np.array: The modified matrix.
    """
    assert matrix.shape[0] == matrix.shape[1], "Input matrix must be square"
    return np.tril(matrix, k)

# Example usage:
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
k = 1
print(zero_above_kth_diagonal(matrix, k))
