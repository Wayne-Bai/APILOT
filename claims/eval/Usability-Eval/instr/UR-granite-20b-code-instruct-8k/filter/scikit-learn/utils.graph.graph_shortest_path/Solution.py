import numpy as np
from scipy.sparse.csgraph import dijkstra

# Define the adjacency matrix of the graph
# For example, a graph with 4 nodes and edges (0, 1), (1, 2), (2, 3) can be represented as:
# adjacency_matrix = np.array([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]])

# Compute the shortest paths using Dijkstra's algorithm
shortest_paths = dijkstra(csgraph=adjacency_matrix, indices=0, return_predecessors=False)

# Print the shortest paths from node 0 to all other nodes
print("Shortest paths from node 0:")
for i in range(len(shortest_paths)):
    print(f"Node {i}: {shortest_paths[i]}")
