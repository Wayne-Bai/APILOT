
import numpy as np
from scipy.linalg import block_diag

# Create a sample matrix
matrix = np.array([[1, 2], [3, 4]])

# Zero out the elements below the 1st diagonal
k = 1
zeros = np.zeros((matrix.shape[0] - k, matrix.shape[1]))
block_diag(matrix, zeros)
