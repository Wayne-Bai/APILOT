import numpy as np

def sign_and_log_determinant(arr):
    # Compute the determinant of the array
    det = np.linalg.det(arr)

    # Compute the sign of the determinant
    sign = np.sign(det)

    # Compute the natural logarithm of the absolute value of the determinant
    log_det = np.log(np.abs(det))

    return sign, log_det
