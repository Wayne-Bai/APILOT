import numpy as np
from scipy.linalg import pinv2

# Define the Hermitian matrix
A = np.array([[1, 2], [2, 4]])

# Compute the pseudo-inverse of A using pinv2
pinv_A = pinv2(A)

print("Pseudo-inverse of A:")
print(pinv_A)
