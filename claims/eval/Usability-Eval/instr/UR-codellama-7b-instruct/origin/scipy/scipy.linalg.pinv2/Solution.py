
import numpy as np
from scipy.linalg import pinv

# Generate a random matrix
A = np.random.rand(5, 3)

# Compute the Moore-Penrose pseudo-inverse of A
pinv_a = pinv(A)

print(pinv_a)
