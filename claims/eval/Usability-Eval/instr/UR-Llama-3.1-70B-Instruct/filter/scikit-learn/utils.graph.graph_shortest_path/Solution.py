import networkx as nx
import numpy as np
from sklearn.utils.graph import graph_shortest_path  # Import the function

# Create an adjacency matrix
adjacency_matrix = np.array([
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0]
])

# Calculate the shortest path matrix
shortest_path_matrix = graph_shortest_path(adjacency_matrix)

# Print the shortest path matrix
print("Shortest Path Matrix:")
print(shortest_path_matrix)

# Alternatively, using NetworkX library for more complex use cases
def calculate_shortest_path(graph):
    return nx.all_pairs_shortest_path_length(graph)

# Create a directed graph
graph = nx.DiGraph()
edges = [(0, 1), (1, 2), (2, 3), (1, 3)]
graph.add_edges_from(edges)

# Calculate the shortest path for all pairs of nodes
shortest_paths = calculate_shortest_path(graph)

# Print the shortest paths
for node, paths in shortest_paths.items():
    print(f"Shortest paths from node {node}:")
    for target_node, length in paths.items():
        print(f"  - {target_node}: {length}")
