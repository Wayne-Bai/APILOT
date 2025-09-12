import numpy as np

# Define your matrix
a = np.array([[1, 2], [3, 4]])

q, r = np.linalg.qr(a)

print("Q:\n", q)
print("\nR:\n", r)
