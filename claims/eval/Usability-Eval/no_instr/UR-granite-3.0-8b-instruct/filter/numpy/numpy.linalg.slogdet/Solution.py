import numpy as np

def sign_and_log_determinant(arr):
    det = np.linalg.det(arr)
    sign = np.sign(det)
    log_det = np.log(np.abs(det))
    return sign, log_det
