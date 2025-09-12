import numpy as np
import networkx as nx
from scipy.sparse import csr_matrix

# Let's start with a scipy sparse matrix
row = np.array([0, 1, 1, 2, 2])
col = np.array([1, 0, 2, 1, 3])
data = np.array([1, 1, 1, 1, 1])
adjacency_matrix = csr_matrix((data, (row, col)), shape=(4, 4))

# Convert the scipy sparse matrix to a networkx graph
graph = nx.from_scipy_sparse_matrix(adjacency_matrix)
