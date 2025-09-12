import networkx as nx
from scipy.sparse import csr_matrix

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])

# Get the adjacency matrix as a SciPy sparse matrix
adjacency_matrix = nx.to_scipy_sparse_matrix(G, format='csr')

# Display the adjacency matrix
print(adjacency_matrix)
