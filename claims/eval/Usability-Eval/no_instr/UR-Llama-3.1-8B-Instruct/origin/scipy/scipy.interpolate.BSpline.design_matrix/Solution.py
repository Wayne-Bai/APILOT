from scipy.sparse import csr_matrix
import numpy as np

# Define the data for the design matrix
n_samples = 10
n_features = 5
data = np.array([1, 2, 3, 4, 5, 0, 0, 6, 7, 8])
row_indices = np.array([0, 0, 1, 1, 2, 2, 3, 3, 4, 4])
col_indices = np.array([0, 1, 0, 2, 2, 3, 0, 3, 1, 4])

# Create the design matrix as a CSR format sparse array
X_csr = csr_matrix((data, (row_indices, col_indices)), shape=(n_samples, n_features))

print(X_csr)
