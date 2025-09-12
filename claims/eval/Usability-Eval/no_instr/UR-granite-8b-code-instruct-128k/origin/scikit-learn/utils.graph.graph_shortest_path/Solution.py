from sklearn.neighbors import NearestNeighbors
import numpy as np

# Assume you have a graph represented as a adjacency matrix
adjacency_matrix = np.array([[0, 1, 0, 0],
                            [1, 0, 1, 0],
                            [0, 1, 0, 1],
                            [0, 0, 1, 0]])

# Create a NearestNeighbors object with the adjacency matrix as the input
nbrs = NearestNeighbors(n_neighbors=2, algorithm='brute').fit(adjacency_matrix)

# Perform a shortest-path graph search starting from node 0
distances, indices = nbrs.kneighbors(adjacency_matrix[0])
print(indices)
