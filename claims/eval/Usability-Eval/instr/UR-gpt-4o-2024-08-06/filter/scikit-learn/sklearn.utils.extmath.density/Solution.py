from scipy import sparse
import numpy as np

# Create a sparse vector
dense_vector = np.array([0, 1, 0, 3, 0, 0, 2, 0, 0, 0])
sparse_vector = sparse.csr_matrix(dense_vector)

# Compute density of the sparse vector
def compute_density(sparse_vector):
    # Number of non-zero elements
    nnz = sparse_vector.nnz
    # Total number of elements in the vector
    total_elements = sparse_vector.shape[1]
    # Calculate density
    density = nnz / total_elements
    return density

# Compute and print the density
density = compute_density(sparse_vector)
print(f"Density of the sparse vector: {density}")
