import networkx as nx
import numpy as np
from scipy import sparse

# Create a scipy sparse matrix adjacency list
adj_matrix = sparse.csr_matrix([
    [0, 1, 1, 0, 0],  # node 0
    [1, 0, 1, 1, 1],  # node 1
    [1, 1, 0, 1, 0],  # node 2
    [0, 1, 1, 0, 1],  # node 3
    [0, 1, 0, 1, 0]   # node 4
])

# Convert the scipy sparse matrix to a networkx graph
G = nx.from_scipy_sparse_array(adj_matrix, directed=False)

# Print the graph
print("Graph Nodes: ", list(G.nodes()))
print("Graph Edges: ", list(G.edges()))
print("Graph Adjacency Matrix: ", nx.to_numpy_array(G))
