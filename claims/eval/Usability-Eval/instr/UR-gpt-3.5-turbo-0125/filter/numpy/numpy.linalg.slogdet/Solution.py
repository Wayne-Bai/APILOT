
import numpy as np

# Create a numpy array
arr = np.array([[1, 2], [3, 4]])

# Compute the sign and natural logarithm of the determinant of the array
sign, logdet = np.linalg.slogdet(arr)

print("Sign of the determinant:", sign)
print("Natural logarithm of the determinant:", logdet)
