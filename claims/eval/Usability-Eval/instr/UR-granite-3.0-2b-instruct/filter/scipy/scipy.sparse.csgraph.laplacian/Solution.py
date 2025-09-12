from scipy.sparse import csr_matrix
from scipy.sparse.linalg import laplacian

# Assuming 'adj_matrix' is the adjacency matrix of the directed graph
# The adjacency matrix is a square matrix used to represent a finite graph.
# The elements of the matrix indicate whether pairs of vertices are adjacent or not in the graph.

# Convert the adjacency matrix to a sparse matrix
adj_matrix_sparse = csr_matrix(adj_matrix)

# Calculate the Laplacian of the graph
laplacian_matrix = laplacian(adj_matrix_sparse)

# The Laplacian matrix is a square matrix used in graph theory, defined as L = D - A,
# where D is the degree matrix and A is the adjacency matrix.
# For a directed graph, the degree matrix D is a diagonal matrix with the degrees of the vertices on the diagonal.
