import networkx as nx
import numpy as np

# Define the adjacency matrix as a numpy array
adj_matrix = np.array([
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
])

# Create a graph from the numpy adjacency matrix
G = nx.from_numpy_array(adj_matrix)

# Print the edges of the graph
print(list(G.edges()))
