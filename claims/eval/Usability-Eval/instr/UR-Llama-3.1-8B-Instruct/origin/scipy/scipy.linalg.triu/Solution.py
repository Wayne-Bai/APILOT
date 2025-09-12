import numpy as np
import scipy

def zero_below_kth_diagonal(matrix, k):
    """
    This function creates a copy of the input matrix with elements below the kth diagonal zeroed.
    
    Parameters:
    matrix (numpy array): The input matrix.
    k (int): The kth diagonal from which elements should be zeroed.
    
    Returns:
    numpy array: The modified matrix with specified diagonals removed.
    """
    
    # Create a copy of the input matrix to avoid modifying the original matrix
    new_matrix = matrix.copy()
    
    # Get the shape of the matrix
    rows, cols = new_matrix.shape
    
    # Calculate the start row and column indices for the current diagonal
    start_row = max(k, 0)
    start_col = max(k, 0)
    
    # Iterate over rows from the start row + 1 to the end of the matrix
    for i in range(start_row + 1, rows):
        # Iterate over columns from the start column to the end of the matrix
        for j in range(start_col, cols):
            # Check if the current element is on the current or lower diagonals
            if abs(i - j) >= k:
                new_matrix[i, j] = 0
    
    return new_matrix

# Example usage:
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
k = 1
print("Original Matrix:")
print(matrix)

new_matrix = zero_below_kth_diagonal(matrix, k)
print("\nMatrix after removing below 1st diagonal:")
print(new_matrix)
