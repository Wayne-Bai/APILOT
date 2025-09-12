
import numpy as np

def zero_above_kth(matrix, k):
    # Get the shape of the matrix
    m, n = matrix.shape
    
    # Create a new matrix with the same shape
    result = np.zeros((m, n), dtype=matrix.dtype)
    
    # Loop through each element in the matrix
    for i in range(m):
        for j in range(n):
            # Check if the element is above the kth diagonal
            if i - j > k:
                # Set the element to 0
                result[i, j] = 0
            else:
                # Leave the element as it is
                result[i, j] = matrix[i, j]
    
    return result
