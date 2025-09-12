import numpy as np

def log_det_sign(matrix):
    # Compute the sign and logarithm of the determinant
    sign, log_det = np.linalg.slogdet(matrix)
    return sign, log_det

# Example usage
matrix = np.array([[1, 2], [3, 4]])
sign, log_det = log_det_sign(matrix)
print("Sign:", sign)
print("Logarithm of determinant:", log_det)
