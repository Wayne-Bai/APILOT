import numpy as np

def construct_matrix(n, m, k):
    """
    Construct (n, m) matrix filled with ones at and below the kth diagonal.
    
    Args:
    n (int): The number of rows in the matrix.
    m (int): The number of columns in the matrix.
    k (int): The diagonal below which the matrix is filled with ones.
    
    Returns:
    A (numpy.ndarray): The constructed matrix.
    """
    # Create an (n, m) matrix filled with zeros.
    A = np.zeros((n, m), dtype=int)
    
    # Iterate over the rows of the matrix.
    for i in range(n):
        # Fill the elements in the current row that are below or on the kth diagonal with ones.
        A[i, min(m, i + k + 1):] = 1
    
    return A

# Example usage:
n = 5
m = 5
k = 2
print(construct_matrix(n, m, k))
