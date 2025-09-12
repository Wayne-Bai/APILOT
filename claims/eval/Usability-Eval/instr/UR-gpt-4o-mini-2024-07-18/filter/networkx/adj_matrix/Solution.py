import networkx as nx
import numpy as np

# Create a graph example
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4)])

# Get the adjacency matrix as a numpy array
adjacency_matrix = nx.to_numpy_array(G)

# Convert to numpy matrix
numpy_matrix = np.matrix(adjacency_matrix)

# Output the numpy matrix
print(numpy_matrix)
