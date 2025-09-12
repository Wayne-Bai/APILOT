import networkx as nx
import numpy as np

# Create a sample numpy matrix
adjacency_matrix = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])

# Create a graph from the numpy matrix
G = nx.from_numpy_matrix(adjacency_matrix)

# Print the nodes in the graph
print(G.nodes())

# Print the edges in the graph
print(G.edges())
