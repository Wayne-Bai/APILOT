import networkx as nx
# create a new DiGraph object
G = nx.DiGraph()
# add nodes and edges to create the prefix tree
G.add_edges_from([(path[0], path[1]) for path in paths])
# print the edges of the prefix tree
print(G.edges())
