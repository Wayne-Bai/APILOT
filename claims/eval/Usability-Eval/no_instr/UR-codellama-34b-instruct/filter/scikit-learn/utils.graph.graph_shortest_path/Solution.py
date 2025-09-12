
import numpy as np
import networkx as nx
from scipy.sparse import csr_matrix

# Create a sample directed graph
G = nx.DiGraph()
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2), (2, 3)])

# Define the source and target nodes
source = 1
target = 3

# Compute the shortest path using NetworkX
shortest_path = nx.shortest_path(G, source, target)

# Convert the shortest path to a sparse matrix
sparse_matrix = csr_matrix((len(shortest_path), len(shortest_path)))
for i in range(len(shortest_path)):
    for j in range(i+1, len(shortest_path)):
        if shortest_path[i] == shortest_path[j]:
            sparse_matrix[i, j] = 1.0

# Print the sparse matrix
print(sparse_matrix)
