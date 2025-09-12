import numpy as np

def qr_factorization(a):
    # Get the number of rows and columns
    m, n = a.shape
    q = np.zeros((m, n))
    r = np.zeros((n, n))

    for j in range(n):
        # Compute the j-th column of q
        v = a[:, j]
        for i in range(j):
            r[i, j] = np.dot(q[:, i], a[:, j])
            v = v - r[i, j] * q[:, i]
        r[j, j] = np.linalg.norm(v)
        q[:, j] = v / r[j, j] if r[j, j] > 0 else v

    return q, r

# Example usage
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
Q, R = qr_factorization(A)
print("Q:\n", Q)
print("R:\n", R)
