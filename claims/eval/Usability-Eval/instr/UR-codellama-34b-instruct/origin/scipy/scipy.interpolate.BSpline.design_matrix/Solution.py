
import numpy as np
from scipy.sparse import csr_matrix

# Define the number of rows and columns in the design matrix
nrows = 10
ncols = 5

# Create a sparse matrix with random values
data = np.random.rand(nrows, ncols)

# Create a CSR format sparse array from the data
X = csr_matrix(data)

print(X)
