import numpy as np

# Define an array
arr = np.array([[1, 2], [3, 4]])

# Compute the determinant
det = np.linalg.det(arr)

# Compute the sign of the determinant
sign_det = np.sign(det)

# Compute the natural logarithm of the determinant
log_det = np.log(det)

print("Sign of the determinant:", sign_det)
print("Logarithm of the determinant:", log_det)
