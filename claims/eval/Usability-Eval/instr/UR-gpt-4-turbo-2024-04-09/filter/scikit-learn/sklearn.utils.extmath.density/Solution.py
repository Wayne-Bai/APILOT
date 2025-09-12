import numpy as np
from scipy.sparse import csr_matrix

def compute_density(sparse_vector):
    # The number of non-zero elements
    non_zero_elements = sparse_vector.nnz
    # The total number of elements in the vector
    total_elements = sparse_vector.size
    # Calculate the density of the sparse vector
    density = non_zero_elements / total_elements
    return density

# Create a sparse vector for example
data = np.array([1, 2, 0, 0, 3, 0, 4, 0, 0, 0])
indices = np.array([0, 1, 4, 6])
indptr = np.array([0, 4])
sparse_vector = csr_matrix((data[indices], indices, indptr), shape=(1, 10))

# Compute the density of the sparse vector
density = compute_density(sparse_vector)
print("Density of the sparse vector:", density)
