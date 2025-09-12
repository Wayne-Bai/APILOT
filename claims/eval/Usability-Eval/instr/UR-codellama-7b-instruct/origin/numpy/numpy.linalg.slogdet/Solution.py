
import numpy as np

def slogdet(A):
    # Compute the sign and natural logarithm of the determinant of an array
    sign, logabsdet = np.linalg.slogdet(A)
    return sign, logabsdet
