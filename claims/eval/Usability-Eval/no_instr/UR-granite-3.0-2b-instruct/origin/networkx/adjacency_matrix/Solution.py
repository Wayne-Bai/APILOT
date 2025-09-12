import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)

# Create an adjacency matrix
adj_matrix = nx.to_numpy(G)

print(adj_matrix)
