
import networkx as nx

# create a simple graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (1, 3), (3, 4)])

# get the adjacency matrix of G
A = nx.adjacency_matrix(G)
print(A)
