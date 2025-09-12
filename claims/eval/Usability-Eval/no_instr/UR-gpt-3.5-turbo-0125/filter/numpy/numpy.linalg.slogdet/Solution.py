
import numpy as np

# Create an example array
arr = np.array([[1, 2], [3, 4]])

# Compute the sign and natural logarithm of the determinant
sign, log_det = np.linalg.slogdet(arr)

print("Sign:", sign)
print("Natural Logarithm of Determinant:", log_det)
