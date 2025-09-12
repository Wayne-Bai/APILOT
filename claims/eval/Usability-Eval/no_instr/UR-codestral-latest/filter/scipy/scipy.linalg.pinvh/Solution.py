import numpy as np
from scipy.linalg import pinvh

# Assume H is your Hermitian matrix
H = np.array([[1, 1j], [-1j, 1]])

# Compute the Moore-Penrose pseudo-inverse
H_pinv = pinvh(H)

# Print the result
print(H_pinv)
