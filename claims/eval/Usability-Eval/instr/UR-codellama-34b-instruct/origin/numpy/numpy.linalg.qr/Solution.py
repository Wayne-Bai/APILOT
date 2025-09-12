import numpy as np

def qr_factorization(a):
    # Compute the QR factorization of the matrix a
    q, r = np.linalg.qr(a)
    return q, r

# Test the function with a sample matrix
a = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]])
q, r = qr_factorization(a)
print(q)
print(r)
