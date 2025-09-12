import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()

# Add some edges
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 1)

# Get the adjacency matrix as a numpy matrix
adjacency_matrix = nx.to_numpy_matrix(G)
print(adjacency_matrix)
