import numpy as np
from numpy import linalg
# Create a sample matrix
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Compute the SVD of the matrix
U, s, Vh = linalg.svd(A)
# Print the results
print("U:", U)
print("s:", s)
print("Vh:", Vh)
