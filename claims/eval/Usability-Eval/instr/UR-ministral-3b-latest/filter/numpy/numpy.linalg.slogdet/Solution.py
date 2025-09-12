import numpy as np

# Create a sample matrix
A = np.array([[1, 2, 2], [3, 4, 4], [5, 6, 6]])

# Calculate the determinant
det = np.linalg.det(A)

# Compute the sign of the determinant
det_sign = np.sign(det)

# Compute the natural logarithm of the determinant
det_log = np.log(det)

print("Determinant:", det)
print("Sign of Determinant:", det_sign)
print("Log of Determinant:", det_log)
