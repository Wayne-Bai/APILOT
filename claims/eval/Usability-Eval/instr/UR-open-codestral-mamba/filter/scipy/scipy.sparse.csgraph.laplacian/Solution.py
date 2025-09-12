import scipy
from scipy.sparse.csgraph import laplacian

# Assuming we have a simple directed graph represented as an adjacency matrix
graph = [[0, 1, 1],
         [1, 0, 1],
         [1, 1, 0]]

# Convert the adjacency matrix to a scipy sparse matrix
sparse_graph = scipy.sparse.csr_matrix(graph)

# Calculate the Laplacian of the directed graph
laplacian_matrix = laplacian(sparse_graph, normed=False)

print(laplacian_matrix.todense())
