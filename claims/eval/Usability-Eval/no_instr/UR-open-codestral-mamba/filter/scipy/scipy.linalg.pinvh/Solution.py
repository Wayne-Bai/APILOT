import scipy.linalg
import numpy as np

# Assuming A as Hermitian matrix
A = np.array([[1, 2+3j], [2-3j, 4]])

# Compute the pseudo-inverse
A_pseudo_inv = scipy.linalg.pinv(A)

print(A_pseudo_inv)
