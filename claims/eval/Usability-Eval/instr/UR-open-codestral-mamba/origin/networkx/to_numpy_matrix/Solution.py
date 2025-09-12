import numpy as np
import networkx as nx

# Create a sample graph for demonstration
G = nx.Graph()
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'D')
G.add_edge('D', 'A')

# Convert the graph to adjacency matrix
adj_matrix = nx.to_numpy_array(G)

print("Adjacency Matrix:")
print(adj_matrix)
