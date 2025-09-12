import numpy as np

def compute_sign_and_log_det(array):
    sign, log_det = np.linalg.slogdet(array)
    return sign, log_det

# Example usage:
array = np.array([[4, 1], [2, 3]])
sign, log_det = compute_sign_and_log_det(array)
print(f"Sign of the determinant: {sign}")
print(f"Natural logarithm of the determinant: {log_det}")
