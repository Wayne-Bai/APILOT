import numpy as np
import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_edges_from([
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 1),
    (2, 4)
])

# Get the adjacency matrix
adj_matrix = nx.to_numpy_matrix(G).todense()

# Convert to numpy matrix
adj_matrix_np = np.array(adj_matrix)

print(adj_matrix_np)
