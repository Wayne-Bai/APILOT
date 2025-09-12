
import numpy as np
from scipy.sparse import coo_matrix
import networkx as nx

# Create a Scipy sparse matrix from an adjacency list
adjacency_list = [[1, 2], [0, 3], [1, 4]]
sparse_matrix = coo_matrix(adjacency_list)

# Convert the sparse matrix to a NetworkX graph
G = nx.from_scipy_sparse_matrix(sparse_matrix)

# Display the graph
print(nx.info(G))
