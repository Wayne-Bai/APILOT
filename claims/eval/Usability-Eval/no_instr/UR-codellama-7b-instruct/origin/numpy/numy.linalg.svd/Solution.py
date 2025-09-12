import numpy as np

def svd(A):
    U, sigma, V = np.linalg.svd(A)
    return U, sigma, V
