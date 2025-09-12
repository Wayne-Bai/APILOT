import networkx as nx
import numpy as np

# Assuming G is your graph
G = nx.Graph()
# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)

# Convert the graph to a numpy matrix
adj_matrix = nx.to_numpy_array(G)

print(adj_matrix)
