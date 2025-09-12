import numpy as np

# Compute the sign and (natural) logarithm of the determinant of an array
def sign_and_log_det(array):
    sign = np.sign(np.linalg.det(array))
    log_det = np.log(np.abs(np.linalg.det(array)))
    return sign, log_det
