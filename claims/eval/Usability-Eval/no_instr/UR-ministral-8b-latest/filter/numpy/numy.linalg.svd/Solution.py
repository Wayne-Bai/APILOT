import numpy as np

A = np.array([[1, 2], [3, 4]])

U, S, Vt = np.linalg.svd(A)

print("U: ", U)
print("S: ", S)
print("V^T: ", Vt)
