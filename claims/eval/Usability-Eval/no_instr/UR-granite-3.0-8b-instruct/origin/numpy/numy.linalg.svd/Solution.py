import numpy as np

# Let's assume we have the following matrix A
A = np.array([[1, 2], [3, 4]])

# Perform Singular Value Decomposition
U, s, VT = np.linalg.svd(A)

# Print the results
print("U = \n", U)
print("s = \n", s)
print("VT = \n", VT)
