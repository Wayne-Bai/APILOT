import numpy as np

# Assuming 'arr' is the input array
arr = np.array([[1, 2], [3, 4]])

# Compute the determinant
det = np.linalg.det(arr)

# Compute the sign and natural logarithm of the determinant
sign_log_det = np.sign(det) * np.log(np.abs(det))

print(sign_log_det)
