import numpy as np

def compute_log_det(matrix):
    # Using numpy.linalg.slogdet to compute the sign and the natural logarithm of the determinant of the matrix
    sign, log_det = np.linalg.slogdet(matrix)
    return sign, log_det

# Example matrix usage
matrix = np.array([[1, 2], [3, 4]])
sign, log_det = compute_log_det(matrix)

print("Sign of the determinant:", sign)
print("Natural logarithm of the determinant:", log_det)
