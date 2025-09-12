import numpy as np
from scipy.sparse import csgraph   # Use scipy for graph operations
from sklearn import linear_model  # Assuming some utility available here

# Create a directed or undirected graph using scipy
A = np.array([[0, 1, 2], [3, 0, 0], [0, 1, 0]])
graph = csgraph.to_scipy_sparse_matrix(A)

# Perform a shortest-path graph search using the bellman algorithm
shortest_paths = csgraph.bellman_distances(graph, directed=True)

print("Shortest paths from each node:", shortest_paths)
