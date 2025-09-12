import numpy as np
from scipy.linalg import diags

def zero_above_kth_diagonal(matrix, k):
    # Create an identity matrix with the same dimensions as the input
    identity = np.eye(*matrix.shape)
    
    # Use diags to create a mask for the kth diagonal, where diags creates a diagonal matrix with ones on the kth diagonal
    mask = diags([1]*matrix.shape[1], k).toarray()
    
    # Multiply the original matrix with the mask to zero out elements above the kth diagonal
    result_matrix = matrix * mask
    
    return result_matrix

# Example usage:
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])
k = 1

new_matrix = zero_above_kth_diagonal(matrix, k)
print(new_matrix)
