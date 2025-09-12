import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2), (2, 3)])

# Convert the graph to an adjacency matrix
A = nx.to_numpy_matrix(G)
print(A)
