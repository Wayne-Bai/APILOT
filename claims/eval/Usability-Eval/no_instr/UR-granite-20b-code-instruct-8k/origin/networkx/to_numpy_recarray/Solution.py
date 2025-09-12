import networkx as nx

# Define the graph
G = nx.Graph()

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)

# Convert the graph to a NumPy recarray
adj_matrix = nx.to_numpy_recarray(G, dtype=[('id', int), ('attr1', float), ('attr2', float)])

# Print the adjacency matrix
print(adj_matrix)
