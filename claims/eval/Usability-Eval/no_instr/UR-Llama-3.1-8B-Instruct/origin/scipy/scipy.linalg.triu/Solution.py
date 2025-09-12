import numpy as np

def zero_below_kth_diagonal(matrix, k):
    """
    Creates a copy of the input matrix where all elements below the kth diagonal are zeroed.
    
    Parameters:
    matrix (numpy array): The input matrix
    k (int): The diagonal index below which elements are zeroed
    
    Returns:
    numpy array: A copy of the input matrix with elements below the kth diagonal zeroed
    """
    
    # Get the number of rows and columns in the matrix
    num_rows, num_cols = matrix.shape
    
    # Create a copy of the input matrix
    result = np.copy(matrix)
    
    # Zero the elements below the kth diagonal
    for i in range(num_rows):
        for j in range(i - k + 1, num_cols):
            result[i, j] = 0
    
    return result

# Example usage:
matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
k = 2
print("Original matrix:")
print(matrix)
print("\nMatrix with elements below the {}th diagonal zeroed:".format(k))
print(zero_below_kth_diagonal(matrix, k))
