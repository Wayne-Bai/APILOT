import numpy as np

# Define the matrix
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

# Define the kth diagonal
k = 1

# Get the dimensions of the matrix
n = A.shape[0]

# Create a new matrix with template of zeros
B = np.zeros((n, n))

# Zero out the elements above the kth diagonal
for i in range(n):
    for j in range(n):
        if j - i > k - 1:
            B[i, j] = 0

# Now, copy elements above the kth diagonal from A to B
for i in range(n):
    for j in range(n):
        if j - i <= k - 1:
            B[i, j] = A[i, j]

print(B)
