import numpy as np

# Create a 2D array
arr = np.array([[1, 2], [3, 4]])

# Compute the determinant
det = np.linalg.det(arr)

# Compute the sign of the determinant
sign = np.sign(det)

# Compute the natural logarithm of the absolute value of the determinant
log_det = np.log(abs(det))

print("Sign of the determinant:", sign)
print("Natural logarithm of the absolute value of the determinant:", log_det)
