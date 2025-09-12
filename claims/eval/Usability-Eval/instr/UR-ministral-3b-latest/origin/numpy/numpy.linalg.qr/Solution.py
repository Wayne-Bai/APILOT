import numpy as np

def compute_qr_factorization(a):
    q, r = np.linalg.qr(a)
    return q, r

# Example usage:
# matrix_to_factorize = np.array([[1, 2], [3, 4], [5, 6]])
# q, r = compute_qr_factorization(matrix_to_factorize)
# print("Q:")
# print(q)
# print("R:")
# print(r)
