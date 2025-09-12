from sklearn.preprocessing import normalize
from scipy.sparse import csr_matrix
import numpy as np

# Create a sparse vector
sparse_vector = csr_matrix(np.array([1, 2, 3, 4, 5]))

# Normalize the sparse vector
normalized_sparse_vector = normalize(sparse_vector, norm='l1', axis=0)

# Compute the density of the normalized sparse vector
density = np.sum(normalized_sparse_vector) / np.prod(normalized_sparse_vector.shape)

print("Density of the normalized sparse vector:", density)
