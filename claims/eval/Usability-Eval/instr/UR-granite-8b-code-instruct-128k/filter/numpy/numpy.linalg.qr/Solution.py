import numpy as np

def qr_factorization(a):
    q, r = np.linalg.qr(a)
    return q, r
