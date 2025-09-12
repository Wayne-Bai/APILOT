# Import necessary libraries
import networkx as nx
import scipy.sparse as sp

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])

# Get the adjacency matrix
adj_matrix = nx.to_scipy_sparse_matrix(G)

# Print the adjacency matrix
print(adj_matrix)

# To save the adjacency matrix to a file
import scipy.io as sio
sio.mmwrite('adj_matrix.mtx', adj_matrix)
