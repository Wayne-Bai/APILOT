import numpy as np

def sign_and_log_determinant(matrix):
    sign, logdet = np.linalg.slogdet(matrix)
    return sign, logdet

# Example usage
array = np.array([[1, 2], [3, 4]])
sign, log_determinant = sign_and_log_determinant(array)
print("Sign:", sign)
print("Logarithm of the determinant:", log_determinant)
