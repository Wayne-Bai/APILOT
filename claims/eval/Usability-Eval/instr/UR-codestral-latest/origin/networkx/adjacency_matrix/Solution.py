# Import the necessary package
import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()
# Add nodes and edges according to your requirements

# Using to_numpy_matrix() function from numpy to convert the adjacency matrix to a numpy array
adj_matrix = nx.to_numpy_matrix(G)

# Print the adjacency matrix
print(adj_matrix)
