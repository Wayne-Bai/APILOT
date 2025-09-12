import numpy as np

# Define a sample array
array = np.array([[1, 2], [3, 4]])

# Compute the determinant
det = np.linalg.det(array)

# Compute the sign and natural logarithm of the determinant
sign_log_det = np.sign(det) * np.log(abs(det))

print("Sign and natural logarithm of the determinant:", sign_log_det)
