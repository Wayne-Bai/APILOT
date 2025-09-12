import networkx as nx

# Create a graph G
G = nx.Graph()

# Add some nodes and edges
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (4, 5), (5, 6)])

# Get the adjacency matrix
adj_matrix = nx.adjacency_matrix(G).todense()

print(adj_matrix)
