import scipy.linalg

# Define a sample matrix
A = [[1, 2], [3, 4], [5, 6]]

# Compute the pseudo-inverse of matrix A
A_pinv = scipy.linalg.pinv(A)

# Print the pseudo-inverse
print(A_pinv)
