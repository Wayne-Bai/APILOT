import numpy as np
from scipy import sparse

# Define the shape of the design matrix
n_rows = 10
n_cols = 5

# Create a random sparse matrix
data = np.random.rand(n_rows, n_cols)
row_indices = np.arange(n_rows)
col_indices = np.arange(n_cols)

# Convert the dense matrix to CSR format
csr_matrix = sparse.csr_matrix((data, (row_indices, col_indices)), shape=(n_rows, n_cols))
