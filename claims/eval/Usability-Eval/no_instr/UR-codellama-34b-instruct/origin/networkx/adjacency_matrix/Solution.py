
import networkx as nx

# Create a simple graph with 3 nodes and 2 edges
G = nx.Graph()
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2), (2, 3)])

# Create an adjacency matrix for the graph
A = nx.to_numpy_matrix(G)
print(A)
