from scipy import sparse
import sklearn.metrics.pairwise as pairwise

# Let's assume you have a sparse vector in CSR format
sparse_vector = sparse.csr_matrix([0, 0, 0, 1, 2, 0, 0, 3])

# Compute the density of a sparse vector
density = (len(sparse_vector.data) / sparse_vector.size) * 100

print(f"The density of the sparse vector is {density}%")
