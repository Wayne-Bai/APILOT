import networkx as nx

# Create a graph (You can modify this part to have a specific graph)
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Calculate the adjacency matrix
adj_matrix = nx.adjacency_matrix(G).todense()

print("Adjacency Matrix:")
print(adj_matrix)
