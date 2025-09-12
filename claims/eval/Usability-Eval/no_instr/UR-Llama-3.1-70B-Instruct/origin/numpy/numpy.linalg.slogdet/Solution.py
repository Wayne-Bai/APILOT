import numpy as np

def compute_sign_and_log_det(array):
    det = np.linalg.det(array)
    sign = np.sign(det)
    log_det = np.log(np.abs(det))
    
    return sign, log_det

# Example usage:
array = np.array([[1, 2], [3, 4]])
sign, log_det = compute_sign_and_log_det(array)

print("Sign of determinant:", sign)
print("Natural logarithm of the absolute value of the determinant:", log_det)
