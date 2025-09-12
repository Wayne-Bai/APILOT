import numpy as np
from scipy.sparse import csr_matrix

# Define the number of rows and columns
n_rows, n_cols = 10, 15

# Create a sparse design matrix
design_matrix = csr_matrix(np.random.rand(n_rows, n_cols))

# Print the design matrix
print(design_matrix.toarray())
