import scipy
from scipy.linalg import svd, pinv
import numpy as np

def calculate_generalized_inverse(matrix, tol=1e-12):
    U, S, Vh = svd(matrix)
    invS = np.where(S > tol, 1.0/S, 0)
    return U @ np.diag(invS) @ Vh

# test the function with a random matrix
matrix = np.array([[1., 2., 3.], [4., 5., 6.]])
print(calculate_generalized_inverse(matrix))
