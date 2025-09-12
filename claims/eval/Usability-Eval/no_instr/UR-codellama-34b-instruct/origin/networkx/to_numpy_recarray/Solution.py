import networkx as nx
import numpy as np

# Create a simple graph with 4 nodes and 3 edges
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4)])

# Get the adjacency matrix of the graph
A = nx.adjacency_matrix(G)

# Convert the adjacency matrix to a NumPy record array
rec_array = np.array([[float(v) for v in row] for row in A], dtype=np.float32)
