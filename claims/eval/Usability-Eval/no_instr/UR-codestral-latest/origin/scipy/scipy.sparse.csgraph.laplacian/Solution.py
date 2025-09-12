import scipy as sp
import networkx as nx

# Create a directed graph
G = nx.DiGraph()
# Add edges to the graph
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Compute the Laplacian of the graph
L = nx.directed_laplacian_matrix(G)

# Print the Laplacian matrix
print(L.todense())
