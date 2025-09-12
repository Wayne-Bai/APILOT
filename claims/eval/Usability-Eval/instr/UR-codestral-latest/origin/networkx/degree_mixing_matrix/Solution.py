import numpy as np
import networkx as nx

# Create a graph
G = nx.Graph()

# Assume nodes and their attributes are defined here
# ...

# Get the adjacency matrix
A = nx.to_numpy_array(G)

# Get the degree matrix
D = np.diag(np.sum(A, axis=1))

# Calculate D^-1/2
D_inv_sqrt = np.diag(1 / np.sqrt(np.diag(D)))

# Calculate the mixing matrix
M = np.dot(np.dot(D_inv_sqrt, A), D_inv_sqrt)

# The mixing matrix M now contains the mixing information for the graph based on its topology
