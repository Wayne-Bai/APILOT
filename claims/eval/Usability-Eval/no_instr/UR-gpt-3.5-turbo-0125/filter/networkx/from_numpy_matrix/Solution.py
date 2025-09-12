
import networkx as nx
import numpy as np

# Create a numpy matrix as the adjacency matrix for the graph
adj_matrix = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])

# Create a graph object from the numpy matrix
G = nx.Graph(adj_matrix)

# Print the graph
print(G.edges())
