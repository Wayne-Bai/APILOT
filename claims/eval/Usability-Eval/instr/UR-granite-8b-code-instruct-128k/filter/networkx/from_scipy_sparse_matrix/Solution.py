import networkx as nx
import scipy.sparse as sp

# Create a scipy sparse matrix adjacency list
adj_list = sp.csr_matrix(([1, 1, 1], ([0, 1, 2], [1, 2, 0])), shape=(3, 3))

# Create a graph from the scipy sparse matrix adjacency list
G = nx.from_scipy_sparse_matrix(adj_list)
