import numpy as np

def compute_sign_and_log_determinant(matrix):
    determinant = np.linalg.det(matrix)
    sign_determinant = np.sign(determinant)
    natural_log_determinant = np.log(np.abs(determinant))
    return sign_determinant, natural_log_determinant

# Example usage:
matrix = np.array([[1, 2], [3, 4]])
sign_determinant, natural_log_determinant = compute_sign_and_log_determinant(matrix)
print("Sign of the determinant:", sign_determinant)
print("Natural logarithm of the determinant:", natural_log_determinant)
