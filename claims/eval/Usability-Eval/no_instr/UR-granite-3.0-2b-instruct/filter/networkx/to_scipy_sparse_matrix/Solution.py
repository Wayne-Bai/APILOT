import networkx as nx
import scipy.sparse as sp

# Assuming G is your graph
G = nx.Graph()

# Convert the graph to an adjacency matrix
adj_matrix = nx.to_numpy_array(G)

# Convert the adjacency matrix to a SciPy sparse matrix
adj_matrix_sparse = sp.csr_matrix(adj_matrix)

print(adj_matrix_sparse)
