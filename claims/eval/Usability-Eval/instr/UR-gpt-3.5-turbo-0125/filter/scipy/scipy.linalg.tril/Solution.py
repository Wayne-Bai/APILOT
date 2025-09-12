
import numpy as np

def zero_above_kth_diag(matrix, k):
    lower_triangular_mask = np.tri(matrix.shape[0], matrix.shape[1], k=k+1)
    return matrix * lower_triangular_mask

# Example usage
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
k = 1
result = zero_above_kth_diag(matrix, k)
print("Original matrix:")
print(matrix)
print("\nResult matrix with elements above the {}th diagonal zeroed:".format(k))
print(result)
