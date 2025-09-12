import numpy as np

def compute_log_det(matrix):
    """
    Computes the sign and the (natural) logarithm of the determinant of a matrix.

    Parameters:
        matrix (np.ndarray): A square numpy array.

    Returns:
        sign (int): Sign of the determinant.
        log_det (float): Natural logarithm of the absolute value of the determinant.
    """
    # Perform an LU decomposition of the matrix
    _, L, U = np.linalg.svd(matrix)

    # The determinant of the matrix is the product of the diagonal elements of U
    diag_U = np.diagonal(U)
    det = np.prod(diag_U)

    # Compute sign and logarithm of the determinant
    sign = np.sign(det)
    if sign == 0:
        log_det = -np.inf
    else:
        log_det = np.log(abs(det))
    
    return sign, log_det

# Example usage:
matrix = np.array([[1, 2], [3, 4]])
sign, log_det = compute_log_det(matrix)
print("Sign:", sign)
print("Logarithm of the determinant:", log_det)
