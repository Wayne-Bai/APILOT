import numpy as np

# Assume A is your matrix
# If you need to create a random matrix, you can uncomment the line below
# A = np.random.rand(3, 3)

# Perform Singular Value Decomposition
U, S, VT = np.linalg.svd(A, full_matrices=False)

# U is a unitary matrix
# S is a 1-D array of the singular values in decreasing order
# VT is the conjugate transpose of the unitary matrix V
