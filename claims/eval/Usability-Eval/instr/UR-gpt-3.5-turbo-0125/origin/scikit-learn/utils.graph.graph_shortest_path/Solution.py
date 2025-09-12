
# Importing necessary libraries
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import connected_components

# Define a function to perform shortest path graph search
def shortest_path_search(graph, start_node):
    graph_csr = csr_matrix(graph)
    dist_matrix, _ = dijkstra(graph_csr, indices=start_node, unweighted=False)
    return dist_matrix

# Example usage
graph = np.array([[0, 1, 2, 0],
                  [1, 0, 0, 1],
                  [2, 0, 0, 3],
                  [0, 1, 3, 0]])

start_node = 0
shortest_distances = shortest_path_search(graph, start_node)
print(shortest_distances)
