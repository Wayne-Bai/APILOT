import numpy as np

def compute_sign_and_log_det(array):
    """
    Compute the sign and (natural) logarithm of the determinant of an array.
    
    Args:
        array (numpy.array): input array
    
    Returns:
        tuple: sign of determinant and natural logarithm of determinant
    """
    # Compute determinant using numpy's linalg.det function
    det = np.linalg.det(array)
    
    # Compute natural logarithm of determinant
    log_det = np.log(np.abs(det))
    
    # Compute sign of determinant
    # If determinant is zero, sign will be undefined, we set it to None in this case
    if det == 0:
        sign = None
    else:
        sign = np.sign(det)
    
    return sign, log_det


# Example usage:
array = np.array([[1, 2], [3, 4]])
sign, log_det = compute_sign_and_log_det(array)

print(f"Sign of determinant: {sign}")
print(f"Natural logarithm of determinant: {log_det}")
