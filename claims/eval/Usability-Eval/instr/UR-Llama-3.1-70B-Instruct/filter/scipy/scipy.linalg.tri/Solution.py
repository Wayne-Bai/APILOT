import scipy.linalg
import numpy as np

def construct_matrix(n, m, k):
    """
    Construct (n, m) matrix filled with ones at and below the kth diagonal.
    
    Args:
    n (int): Number of rows.
    m (int): Number of columns.
    k (int): Diagonal number.
    
    Returns:
    np.ndarray: (n, m) matrix filled with ones at and below the kth diagonal.
    """
    # Initialize a matrix filled with zeros
    matrix = np.zeros((n, m))
    
    # Iterate over each row
    for i in range(n):
        # Iterate over each column
        for j in range(m):
            # Check if the current element is at or below the kth diagonal
            if j <= i + k:
                # Fill the current element with one
                matrix[i, j] = 1
    
    return matrix

# Example usage
n = 5
m = 5
k = 2

result_matrix = construct_matrix(n, m, k)
print(result_matrix)
