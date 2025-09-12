import networkx as nx
import numpy as np

# Sample adjacency matrix
adjacency_matrix = np.array([
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
])

# Create a graph from the adjacency matrix
graph = nx.Graph()

# Add nodes
num_nodes = adjacency_matrix.shape[0]
graph.add_nodes_from(range(num_nodes))

# Add edges based on adjacency matrix
for i in range(num_nodes):
    for j in range(num_nodes):
        if adjacency_matrix[i, j] != 0:
            graph.add_edge(i, j)

# Output to check the structure of the graph
print("Nodes in the graph:", list(graph.nodes))
print("Edges in the graph:", list(graph.edges))
