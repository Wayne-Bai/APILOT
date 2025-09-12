import networkx as nx
from scipy.sparse import csr_matrix

# Create a graph
G = nx.Graph()

# Add some nodes and edges
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 1)
G.add_edge(2, 4)

# Get the adjacency matrix as a SciPy sparse matrix
adjacency_sparse_matrix = nx.adjacency_matrix(G)

# Convert to a csr_matrix if needed (adjacency_matrix already returns csr_matrix)
adjacency_sparse_csr = csr_matrix(adjacency_sparse_matrix)

print(adjacency_sparse_csr)
