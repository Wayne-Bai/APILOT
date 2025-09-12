import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()

# Add some edges to the graph
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)

# Get the adjacency matrix as a numpy matrix
adjacency_matrix = nx.to_numpy_matrix(G)
print(adjacency_matrix)
