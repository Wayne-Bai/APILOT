import numpy as np
from scipy.sparse import csr_matrix

# Generate a sparse vector, for example with mostly zeros
dense_vector = np.array([0, 0, 3, 0, 4, 0, 0, 0, 5, 0])
sparse_vector = csr_matrix(dense_vector)

# Function to compute density of a sparse vector
def compute_density(sparse_vec):
    # Get the number of non-zero entries
    num_nonzero = sparse_vec.nnz
    # Get the total number of entries
    total_entries = sparse_vec.shape[1]
    # Compute the density
    density = num_nonzero / total_entries
    return density

# Calculate the density
density = compute_density(sparse_vector)
print("Density of the sparse vector:", density)
