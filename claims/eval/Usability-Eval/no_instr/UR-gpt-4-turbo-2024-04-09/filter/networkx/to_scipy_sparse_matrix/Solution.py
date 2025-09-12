import networkx as nx

# Create a graph
G = nx.Graph()

# Add some edges
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])

# Get the adjacency matrix as a SciPy sparse matrix
adj_matrix = nx.adjacency_matrix(G)
print(adj_matrix)
