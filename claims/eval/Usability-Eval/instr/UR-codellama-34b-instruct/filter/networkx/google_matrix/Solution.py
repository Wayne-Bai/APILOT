
import networkx as nx

# create a simple graph with three nodes and two edges
G = nx.Graph()
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2), (2, 3)])

# compute the Google matrix of the graph
google_matrix = nx.to_numpy_matrix(G)
print(google_matrix)
