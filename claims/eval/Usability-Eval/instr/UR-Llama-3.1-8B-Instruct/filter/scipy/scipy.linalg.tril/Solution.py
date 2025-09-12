import numpy as np

def zero_above_kth_diagonal(matrix, k):
    # Create a copy of the matrix
    mat_copy = matrix.copy()
    
    # Get the number of rows and columns in the matrix
    rows, cols = mat_copy.shape
    
    # Iterate over the rows and columns
    for i in range(rows):
        for j in range(cols):
            # Calculate the diagonal number (lower triangle is considered as positive)
            if j - i <= k:
                # If the element is above the kth diagonal, set it to zero
                mat_copy[i, j] = 0
                
    return mat_copy

# Example usage:
matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
k = 1
print("Original matrix:")
print(matrix)
print("\nMatrix with k = {} diagonal zeroed above the kth diagonal:".format(k))
print(zero_above_kth_diagonal(matrix, k))
