
from sklearn.preprocessing import sparse
import numpy as np

# Create a sparse matrix from an array
A = sparse.csr_matrix(np.array([[0, 1, 2], [3, 4, 5]]))

# Compute the density of the sparse matrix
density = A.density()

print("Density:", density)
