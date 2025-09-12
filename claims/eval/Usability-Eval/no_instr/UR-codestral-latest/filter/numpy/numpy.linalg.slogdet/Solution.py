import numpy as np

def log_determinant(matrix):
    det = np.linalg.det(matrix)
    if det > 0:
        sign = 1
        log_det = np.log(det)
    elif det < 0:
        sign = -1
        log_det = np.log(-det)
    else:
        sign = 0
        log_det = float('-inf')
    return sign, log_det

# Example usage:
matrix = np.array([[1, 2], [3, 4]])
sign, log_det = log_determinant(matrix)
print(f"Sign: {sign}, Log Determinant: {log_det}")
