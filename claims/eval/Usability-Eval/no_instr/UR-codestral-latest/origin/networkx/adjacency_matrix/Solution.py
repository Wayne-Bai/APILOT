import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

# Get adjacency matrix
adj_matrix = nx.adjacency_matrix(G)

print(adj_matrix.todense())
