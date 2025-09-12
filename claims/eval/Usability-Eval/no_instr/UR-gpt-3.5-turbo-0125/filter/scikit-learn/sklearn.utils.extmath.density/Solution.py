
# Importing the necessary modules
from scipy.sparse import csr_matrix
import numpy as np

# Creating a sparse vector
data = np.array([0, 0, 0, 1, 2, 0, 3, 0, 0])
indices = np.array([3, 4, 6])
indptr = np.array([0, 3, 3])

sparse_vector = csr_matrix((data, indices, indptr), shape=(1, 9))

# Computing the density of the sparse vector
density = sparse_vector.sum() / sparse_vector.shape[1]
print("Density of the sparse vector:", density)
