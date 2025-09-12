from sklearn.preprocessing import normalize
from scipy.sparse import csr_matrix

# Creating a sparse vector using csr_matrix
sparse_vector = csr_matrix([0, 0, 1, 0, 2, 0, 0, 0, 3])

# Compute the density of a sparse vector
total_elements = sparse_vector.size
non_zero_elements = sparse_vector.count_nonzero()
density = non_zero_elements / total_elements

print("Density of the sparse vector:", density)
