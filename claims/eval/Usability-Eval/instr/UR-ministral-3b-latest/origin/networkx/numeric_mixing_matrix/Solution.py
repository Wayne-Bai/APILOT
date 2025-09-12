import networkx as nx

# Define your graph
G = nx.Graph()

# Add nodes and edges
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

print("Adjacency Matrix for G:")
print(nx.to_numpy_matrix(G))
