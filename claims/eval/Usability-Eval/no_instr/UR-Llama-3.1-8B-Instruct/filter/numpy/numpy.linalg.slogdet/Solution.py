import numpy as np
import numpy.linalg

def compute_sign_and_log_determinant(array):
    """
    Compute the sign and (natural) logarithm of the determinant of an array.

    Parameters:
    array (numpy.ndarray): Input array for which to compute the determinant.

    Returns:
    tuple: A tuple containing the sign and the natural logarithm of the determinant.
    """
    
    # Check if the input array is a square matrix (i.e., has the same number of rows and columns)
    if array.shape[0]!= array.shape[1]:
        raise ValueError("Input array must be a square matrix")
    
    # Compute the determinant of the array
    det = np.linalg.det(array)
    
    # Compute the sign of the determinant (1 for positive, -1 for negative)
    sign = np.sign(det)
    
    # Compute the natural logarithm of the absolute value of the determinant (to avoid NaN for zero determinant)
    log_det = np.log(np.abs(det))
    
    return sign, log_det

# Example usage:
array = np.array([[1, 2], [3, 4]])
sign, log_determinant = compute_sign_and_log_determinant(array)
print(f"Sign: {sign}, Natural logarithm of determinant: {log_determinant}")
