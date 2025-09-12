from sklearn.metrics import pairwise_distances
import numpy as np

# Assuming graph is represented as an adjacency matrix
graph = np.array([[0, 1, 2, 0], [1, 0, 0, 3], [2, 0, 0, 3], [0, 3, 3, 0]])

# Shortest path from a single source (Dijkstra's algorithm)
start_node = 0
shortest_distances = pairwise_distances(graph, metric='precomputed')[start_node]

# Shortest path between all pairs of nodes (Floyd-Warshall's algorithm)
shortest_distances_all_pairs = pairwise_distances(graph, metric='precomputed')
np.fill_diagonal(shortest_distances_all_pairs, 0)
for k in range(len(graph)):
    for i in range(len(graph)):
        for j in range(len(graph)):
            shortest_distances_all_pairs[i][j] = min(shortest_distances_all_pairs[i][j], shortest_distances_all_pairs[i][k] + shortest_distances_all_pairs[k][j])
