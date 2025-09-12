
import numpy as np

def zero_below_kth_diagonal(matrix, k):
    result = np.array(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j - i > k:
                result[i][j] = 0
    return result

# Example usage
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
k = 1
new_matrix = zero_below_kth_diagonal(matrix, k)
print("Original Matrix:")
print(matrix)
print("Matrix with elements below the", k, "th diagonal zeroed:")
print(new_matrix)
