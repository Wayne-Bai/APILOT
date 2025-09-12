import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(3, 4)

# Convert the graph to an adjacency matrix
adj_matrix = nx.to_numpy_array(G)

# Print the adjacency matrix
print(np.matrix(adj_matrix))
