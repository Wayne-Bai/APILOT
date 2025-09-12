
import numpy as np

def sign_log_det(arr):
    """
    Computes the sign and (natural) logarithm of the determinant of an array.

    Parameters:
        arr (numpy.ndarray): The input array.

    Returns:
        tuple: A tuple containing the sign and natural logarithm of the determinant of the array.
    """
    det = np.linalg.det(arr)
    if det < 0:
        sign = -1
    else:
        sign = 1
    return sign, np.log(abs(det))
