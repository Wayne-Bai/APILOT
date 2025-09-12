from sklearn.sparse import csr_matrix, reduce_dimension

# Create a sparse vector example
sparse_vector = csr_matrix(([1, 2, 3], ([0, 2, 4], [1, 2, 3])))

# Compute the density of the sparse vector
density = 1 - reduce_dimension(sparse_vector, 3).toarray().mean()

print(density)
