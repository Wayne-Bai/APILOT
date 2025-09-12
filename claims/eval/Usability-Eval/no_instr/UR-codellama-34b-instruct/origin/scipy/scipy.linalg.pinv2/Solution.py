
import numpy as np
from scipy.linalg import pinv, svd

# Define the matrix A for which we want to compute the pseudo-inverse
A = np.array([[1, 2], [3, 4]])

# Compute the singular value decomposition (SVD) of A
U, sigma, Vt = svd(A)

# Compute the Moore-Penrose pseudo-inverse of A
pinv_A = np.dot(Vt.T, np.dot(np.diag(1.0 / sigma), U.T))

# Print the result
print(pinv_A)
