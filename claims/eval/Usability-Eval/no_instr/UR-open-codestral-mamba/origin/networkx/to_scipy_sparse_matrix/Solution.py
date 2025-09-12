import networkx as nx
import scipy.sparse as sp

# Create a graph
G = nx.Graph()

# Add edges to the graph. Nodes are automatically added if they don't exist.
edges = [(0, 1), (1, 2), (1, 3), (3, 4), (3, 5)]
G.add_edges_from(edges)

# Convert the adjacency matrix of the graph to a SciPy sparse matrix
adjacency_matrix = nx.adjacency_matrix(G)
sparse_adjacency_matrix = sp.csr_matrix(adjacency_matrix)

print(sparse_adjacency_matrix.toarray())
