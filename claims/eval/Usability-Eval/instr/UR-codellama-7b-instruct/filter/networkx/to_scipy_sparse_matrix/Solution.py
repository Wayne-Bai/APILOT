
import networkx as nx

# Create a simple graph
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 1)

# Return the adjacency matrix as a SciPy sparse matrix
A = nx.to_scipy_sparse_matrix(G)
