import numpy as np

def compute_log_det(array):
    # Compute the LU decomposition
    lu, piv = np.linalg.lu_factor(array)
    
    # Compute the sign of the determinant from the number of row swaps
    sign = (-1) ** np.count_nonzero(piv != np.arange(array.shape[0]))
    
    # Compute the natural logarithm of the absolute determinant
    log_det = np.sum(np.log(np.abs(np.diag(lu))))
    
    return sign, log_det

# Example usage:
array = np.array([[4, 1], [2, 3]])
sign, log_det = compute_log_det(array)
print(f"Sign of the determinant: {sign}")
print(f"Natural logarithm of the determinant: {log_det}")
