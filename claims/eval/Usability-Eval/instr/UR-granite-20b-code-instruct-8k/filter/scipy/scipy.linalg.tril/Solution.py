import numpy as np
import scipy

# Input matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Output matrix with elements above the kth diagonal zeroed
k = 1
output_matrix = scipy.linalg.circulant(matrix, k)

print(output_matrix)
