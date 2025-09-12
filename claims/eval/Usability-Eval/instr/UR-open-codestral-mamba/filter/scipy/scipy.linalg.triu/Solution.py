import scipy
import numpy as np

def zero_below_kth_diagonal(matrix, k):
    '''Function to zero elements below the kth diagonal'''

    # Get the shape of the matrix
    row, col = matrix.shape

    # Create an array of ones with the same shape as the matrix
    mask = np.ones((row, col), dtype=np.bool)

    # Create a triangular matrix with ones in the kth diagonal and below it
    mask = np.tril(mask, k=k)

    # Zero elements below the kth diagonal
    matrix = matrix * mask

    return matrix

# Test the function
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
k = 1
print(zero_below_kth_diagonal(A, k))
