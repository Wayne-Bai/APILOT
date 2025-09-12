import numpy as np
import scipy

def zero_below_kth_diagonal(matrix, k):
    # Create a copy of the original matrix
    result_matrix = np.copy(matrix)
    
    # Get the shape of the matrix
    rows, cols = result_matrix.shape
    
    # Iterate through the matrix and zero out elements below the kth diagonal
    for i in range(rows):
        for j in range(cols):
            if i - j > k:
                result_matrix[i, j] = 0
                
    return result_matrix

# Example usage
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

k = 1
new_matrix = zero_below_kth_diagonal(matrix, k)
print(new_matrix)
