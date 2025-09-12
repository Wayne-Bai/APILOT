import numpy as np
import scipy

def zero_below_kth_diagonal(matrix, k):
    # Create a copy of the original matrix
    matrix_copy = np.copy(matrix)
    
    # Get the number of rows and columns
    rows, cols = matrix_copy.shape
    
    # Zero out elements below the k-th diagonal
    for i in range(rows):
        for j in range(cols):
            if i > j + k:  # Condition to check if below the k-th diagonal
                matrix_copy[i, j] = 0
    
    return matrix_copy

# Example Usage
original_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
k = 1
result = zero_below_kth_diagonal(original_matrix, k)
print(result)
