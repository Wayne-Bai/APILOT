import numpy as np

def log_det_sign(matrix):
    # Ensure the matrix is a numpy array
    matrix = np.asarray(matrix)
    
    # Compute the eigenvalues
    eigenvalues = np.linalg.eigvals(matrix)
    
    # Compute the sign of the determinant
    sign = np.sign(np.prod(eigenvalues))
    
    # Compute the natural logarithm of the absolute value of the determinant
    log_det = np.log(np.abs(np.prod(eigenvalues)))
    
    return sign, log_det

# Example usage
matrix = np.array([[1, 2], [3, 4]])
sign, log_det = log_det_sign(matrix)
print(f"Sign: {sign}, Log Determinant: {log_det}")
