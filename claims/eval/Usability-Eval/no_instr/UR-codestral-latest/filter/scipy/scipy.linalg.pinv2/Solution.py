import numpy as np
from scipy.linalg import pinv

# Let's define a matrix
A = np.array([[1, 2, 3], [4, 5, 6]])

# Compute the Moore-Penrose pseudo-inverse
A_pinv = pinv(A)

print("The original matrix is:")
print(A)
print("The pseudo-inverse is:")
print(A_pinv)
