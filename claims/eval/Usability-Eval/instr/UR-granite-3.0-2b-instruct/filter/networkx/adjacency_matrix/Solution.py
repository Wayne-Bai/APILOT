import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(5, 1)

# Get the adjacency matrix
adj_matrix = nx.to_numpy(G.to_adj())

print(adj_matrix)
