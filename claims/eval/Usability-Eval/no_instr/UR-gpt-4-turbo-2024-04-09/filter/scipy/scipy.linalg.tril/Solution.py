import scipy.linalg
import numpy as np

def zero_above_kth_diagonal(matrix, k):
    # Use the tril function from scipy.linalg, which returns the lower triangle of the matrix
    return scipy.linalg.tril(matrix, k=k)

# Example usage:
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
k = 0  # Specify the k-th diagonal
new_matrix = zero_above_kth_diagonal(matrix, k)
print(new_matrix)
