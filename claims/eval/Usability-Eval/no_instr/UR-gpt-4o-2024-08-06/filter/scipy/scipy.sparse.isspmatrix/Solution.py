from scipy.sparse import issparse

# Example sparse matrix
from scipy.sparse import csr_matrix

# Create a sparse matrix
sparse_matrix = csr_matrix([[1, 0, 0], [0, 0, 3]])

# Check if the matrix is sparse
is_sparse = issparse(sparse_matrix)

print("Is the matrix sparse?", is_sparse)
