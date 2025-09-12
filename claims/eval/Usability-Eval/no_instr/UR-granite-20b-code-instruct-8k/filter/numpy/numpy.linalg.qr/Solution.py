import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
q, r = np.linalg.qr(a)

print("Q:\n", q)
print("R:\n", r)
