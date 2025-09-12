import networkx as nx
import scipy.sparse as sp

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Get the adjacency matrix as a SciPy sparse matrix
adj_matrix = nx.to_scipy_sparse_matrix(G)

print(adj_matrix)
