import networkx as nx
import scipy.sparse as sp

# Create a sample graph
G = nx.Graph()

# Add edges to the graph
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (2, 4)])

# Generate adjacency matrix
adj_matrix = nx.to_scipy_sparse_matrix(G)

# Print adjacency matrix
print(adj_matrix.todense())
