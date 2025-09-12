
import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])

# Generate the adjacency matrix
adj_matrix = nx.to_numpy_matrix(G)

print(adj_matrix)
