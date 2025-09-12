import numpy as np
from scipy.sparse.csgraph import shortest_path
from scipy.sparse import csr_matrix

# Example adjacency matrix for a directed graph
# Replace this with your actual graph data
adjacency_matrix = np.array([
    [0, 1, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 3],
    [4, 0, 0, 0]
])

# Convert the adjacency matrix to a sparse matrix
sparse_graph = csr_matrix(adjacency_matrix)

# Perform the shortest path search
# 'directed=True' for directed graph, 'directed=False' for undirected graph
dist_matrix, predecessors = shortest_path(sparse_graph, directed=True, return_predecessors=True)

# Print the shortest path distances
print("Shortest path distances:")
print(dist_matrix)

# Print the predecessors matrix
print("Predecessors:")
print(predecessors)
