import numpy as np

def qr_factorization(a):
    # Compute the QR factorization of the matrix a
    q, r = np.linalg.qr(a)
    
    return q, r

# Example usage
a = np.array([[1, 2], [3, 4]])
q, r = qr_factorization(a)
print("Q:")
print(q)
print("\nR:")
print(r)