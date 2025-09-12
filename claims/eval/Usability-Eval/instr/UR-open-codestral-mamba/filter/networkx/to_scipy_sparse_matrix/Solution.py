import networkx as nx
import scipy.sparse as sp

# Create a graph
G = nx.Graph()

# Add edges to the graph
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]
G.add_edges_from(edges)

# Convert the adjacency matrix to a sparse matrix
adj_matrix = nx.to_scipy_sparse_matrix(G)

print(adj_matrix.toarray())
