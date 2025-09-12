import numpy as np

# Let's create a 3x3 matrix
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Perform SVD
U, s, VT = np.linalg.svd(A, full_matrices=True)

# Now U, s, and VT contain the singular values and singular vectors
print("U = \n", U)
print("s = \n", s)
print("VT = \n", VT)
