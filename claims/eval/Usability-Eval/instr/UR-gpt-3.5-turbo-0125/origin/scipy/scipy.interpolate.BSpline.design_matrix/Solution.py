
import numpy as np
from scipy.sparse import csr_matrix

# Define matrix values
data = np.array([1, 2, 3, 4, 5, 6])
indices = np.array([0, 2, 2, 1, 3, 2])
indptr = np.array([0, 2, 3, 6])

# Create CSR sparse matrix
design_matrix = csr_matrix((data, indices, indptr), shape=(3, 4))

print(design_matrix)
