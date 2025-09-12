import scipy.linalg as la
import numpy as np

def zero_below_kth_diagonal(matrix, k):
    result = np.triu(matrix, k=k)
    return result

# Example matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# k value (diagonal)
k = 1  # Zero elements below the first diagonal

# Create a new matrix with elements below the kth diagonal zeroed
new_matrix = zero_below_kth_diagonal(matrix, k)

print(new_matrix)
