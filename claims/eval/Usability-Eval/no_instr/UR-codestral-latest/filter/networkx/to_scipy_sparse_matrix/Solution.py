import networkx as nx
from scipy import sparse

# Create a graph
G = nx.Graph()

# Add some edges
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])

# Convert graph to adjacency matrix
adj_matrix = nx.to_scipy_sparse_matrix(G)

# Print the adjacency matrix
print(adj_matrix)
