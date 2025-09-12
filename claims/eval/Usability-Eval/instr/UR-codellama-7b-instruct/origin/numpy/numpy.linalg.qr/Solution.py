
import numpy as np

# compute QR factorization of a matrix
def qr_factorization(a):
    # compute QR decomposition using Householder reflections
    q, r = np.linalg.qr(a)
    
    # make sure Q is orthonormal by normalizing its columns
    q /= np.sqrt(np.sum(q * q, axis=0))
    
    return q, r
