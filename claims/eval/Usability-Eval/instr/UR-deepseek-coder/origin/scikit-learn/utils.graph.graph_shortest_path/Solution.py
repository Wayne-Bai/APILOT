import numpy as np
from sklearn.neighbors import kneighbors_graph
from scipy.sparse.csgraph import shortest_path

# Example adjacency matrix (replace this with your actual graph data)
adjacency_matrix = np.array([
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
])

# Convert the adjacency matrix to a sparse graph
sparse_graph = kneighbors_graph(adjacency_matrix, mode='distance')

# Perform the shortest path search
dist_matrix, predecessors = shortest_path(sparse_graph, directed=False, return_predecessors=True)

# Output the distance matrix and predecessors
print("Distance Matrix:")
print(dist_matrix)
print("Predecessors:")
print(predecessors)
