import numpy as np

def qr_factorization(a):
    q, r = np.linalg.qr(a)
    return q, r

# Example usage
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
q, r = qr_factorization(a)

print("QR Factorization Result:")
print("Q:")
print(q)
print("R:")
print(r)
