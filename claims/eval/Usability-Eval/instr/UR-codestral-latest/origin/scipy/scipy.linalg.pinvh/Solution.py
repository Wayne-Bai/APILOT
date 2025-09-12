import numpy as np
import scipy.linalg

# Let's define a Hermitian matrix
A = np.array([[1, 2j, 3], [-2j, 4, 5j], [3, -5j, 6]])
A = (A + A.T.conj()) / 2.0

# Compute the Moore-Penrose pseudo-inverse
pinv = np.linalg.pinv(A)

print(pinv)
