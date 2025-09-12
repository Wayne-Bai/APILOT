
import networkx as nx

# create a simple graph
G = nx.Graph()
G.add_edges_from([(0,1), (0,2), (1,3), (2,4), (3,4)])

# create the adjacency matrix as a NumPy recarray
adj_matrix = nx.to_numpy_recarray(G)
print(adj_matrix)
