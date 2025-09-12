import networkx as nx
from scipy.sparse import csr_matrix

# Assuming 'G' is your NetworkX graph
adj_matrix = nx.to_numpy_array(G)

# Convert the numpy array to a SciPy sparse matrix
sparse_matrix = csr_matrix(adj_matrix)
