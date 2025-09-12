import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)

# Create an adjacency matrix
adj_matrix = nx.adjacency_matrix(G)

# Convert the adjacency matrix to a NumPy matrix
adj_matrix_np = np.array(adj_matrix.data)

print(adj_matrix_np)
