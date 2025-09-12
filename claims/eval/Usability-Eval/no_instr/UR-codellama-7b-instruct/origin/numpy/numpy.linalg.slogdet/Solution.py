
import numpy as np

# Define a random 3x3 matrix
A = np.random.rand(3, 3)

# Compute the determinant of A
det_A = np.linalg.det(A)

# Compute the sign of det_A
sign_det_A = np.sign(det_A)

# Compute the natural logarithm of det_A
log_det_A = np.log(det_A)

print("Sign of determinant:", sign_det_A)
print("Natural logarithm of determinant:", log_det_A)
