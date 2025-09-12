import numpy as np
from scipy.linalg import svd

def generalized_inverse(A, tol=1e-12):
    U, s, Vh = svd(A, full_matrices=False)
    rcond = np.count_nonzero(s > tol)
    s = np.diag(s[:rcond])
    V = Vh[:rcond, :]
    return np.dot(V, np.dot(np.diag(1 / s), U.T))
