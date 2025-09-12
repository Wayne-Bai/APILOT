# Importing scipy library
import scipy
import numpy as np

# Define the kth diagonal
k = 0  # for example

# Create a random matrix
mat = np.random.rand(5, 5)

# Zero out elements above the kth diagonal
mat = scipy.linalg.triu(mat, k)

print(mat)
