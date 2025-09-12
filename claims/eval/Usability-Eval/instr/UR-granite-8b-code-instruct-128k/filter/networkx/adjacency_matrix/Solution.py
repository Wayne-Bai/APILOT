import networkx as nx

# Create a simple graph
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)

# Generate the adjacency matrix
adj_matrix = nx.to_numpy_matrix(G)

print(adj_matrix)
