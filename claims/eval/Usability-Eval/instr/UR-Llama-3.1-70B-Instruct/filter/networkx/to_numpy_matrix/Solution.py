import networkx as nx
import numpy as np

# Create an empty graph
G = nx.Graph()

# Add edges to the graph
G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('B', 'D')
G.add_edge('C', 'D')

# Return the graph adjacency matrix as a NumPy matrix
adj_matrix = nx.to_numpy_array(G)

print(adj_matrix)
