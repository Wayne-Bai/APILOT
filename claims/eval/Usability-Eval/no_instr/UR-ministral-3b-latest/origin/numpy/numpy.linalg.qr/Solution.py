import numpy as np
A = np.array([[1, 2], [3, 4]])
Q, R = np.linalg.qr(A)
print("Q\n", Q)
print("R\n", R)
