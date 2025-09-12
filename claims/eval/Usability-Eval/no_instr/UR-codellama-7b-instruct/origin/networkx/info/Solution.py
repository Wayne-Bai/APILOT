
import networkx as nx

# create a sample graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])

# print short summary of information for the graph G
print(nx.info(G))
