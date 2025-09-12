from scipy import linalg
import numpy as np

def zero_below_diagonal(mat, k):
    """
    Zero elements below the kth diagonal of a matrix.

    Parameters:
    - mat: 2D numpy array or matrix
    - k: int, specifies which diagonal to zero elements below

    Returns:
    - A new matrix with elements below the k-th diagonal zeroed out.
    """
    nrows, ncols = mat.shape
    zeroed_matrix = np.zeros_like(mat)
    
    # Copy elements from the original matrix to the new one, zeroing out below the kth diagonal
    for i in range(nrows):
        for j in range(ncols):
            # Condition to keep the elements coming from the kth diagonal and above
            if j - i >= k:
                zeroed_matrix[i, j] = mat[i, j]

    return zeroed_matrix

# Example usage
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

k = 1
result_matrix = zero_below_diagonal(matrix, k)
print("Original matrix:")
print(matrix)
print("\nMatrix with elements below the 1st diagonal zeroed:")
print(result_matrix)
