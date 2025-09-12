import networkx as nx
from networkx.algorithms import matching

# create an example graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])

# compute a minimum-weight maximal matching of G
matching = matching.maximal_matching(G)
print("Maximal matching:", matching)
