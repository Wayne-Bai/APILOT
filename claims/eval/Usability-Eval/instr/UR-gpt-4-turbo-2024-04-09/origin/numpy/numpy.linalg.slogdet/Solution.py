import numpy as np

def compute_sign_and_logdet(array):
    # Compute the LU decomposition of the array
    lu, piv = np.linalg.lu_factor(array)
    # Get the diagonal elements
    diag = np.diag(lu)
    # Calculate the sign of the determinant
    sign = np.prod(np.sign(diag)) * (-1) ** np.sum(piv != np.arange(len(piv)))
    # Calculate the natural logarithm of the absolute determinant
    log_det = np.sum(np.log(np.abs(diag)))
    return sign, log_det

# Example usage
A = np.array([[1, 2], [3, 4]])
sign, log_det = compute_sign_and_logdet(A)
print("Sign:", sign)
print("Logarithm of the determinant:", log_det)
