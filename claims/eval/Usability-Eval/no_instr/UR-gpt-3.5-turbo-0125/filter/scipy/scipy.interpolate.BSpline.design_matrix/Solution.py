
import numpy as np
from scipy.sparse import csr_matrix

# Assuming X is the design matrix in dense format
X = np.array([[1, 2, 0], [0, 1, 1], [3, 0, 2]])

# Convert the dense matrix X to a CSR sparse matrix
X_csr = csr_matrix(X)

print(X_csr)
