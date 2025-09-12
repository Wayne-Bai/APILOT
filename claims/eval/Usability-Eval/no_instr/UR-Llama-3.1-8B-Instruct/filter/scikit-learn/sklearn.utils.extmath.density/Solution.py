# Import necessary libraries from scikit-learn
from sklearn import metrics
import numpy as np
from scipy import sparse

# Create a sparse matrix (vector in this case)
sparse_vector = sparse.csr_matrix([0, 10, 0, 20])

# Compute the density of the sparse vector
density = 1 - (sparse_vector.nnz / sparse_vector.shape[0])

print(f"Density of the sparse vector: {density}")
