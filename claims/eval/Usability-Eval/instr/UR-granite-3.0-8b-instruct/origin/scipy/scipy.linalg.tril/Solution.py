import numpy as np

def zero_above_kth_diagonal(matrix, k):
    n = matrix.shape[0]
    diag = np.diag(np.diag(matrix, k))
    return matrix - diag

# Example usage:
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])
k = 1
result = zero_above_kth_diagonal(matrix, k)
print(result)
