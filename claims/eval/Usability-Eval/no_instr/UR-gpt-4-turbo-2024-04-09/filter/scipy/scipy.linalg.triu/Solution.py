import numpy as np
from scipy.linalg import triu

def zero_elements_below_kth_diagonal(matrix, k):
    # Use triu to zero out elements below the k-th diagonal
    upper_tri_matrix = triu(matrix, k=k)
    return upper_tri_matrix

# Example usage
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

k = 1  # Specify the k-th diagonal
result = zero_elements_below_kth_diagonal(A, k)
print(result)
