import numpy as np

# Assuming matrix is a numpy array
matrix = np.constraints.asarray([1, 2, 3, 4, 5, 6, 7])  # Example matrix
k = 2  # kth diagonal to be considered

# Number of rows or columns in the matrix
n = matrix.shape[0]

# Create an array with zeros below the kth diagonal
copy_matrix = np.zeros((n, n))

# Fill the matrix with values, but zero the elements below the kth diagonal
copy_matrix[:, k:] = matrix[:, k:]
copy_matrix[:k, k:] = 0

print(copy_matrix)
