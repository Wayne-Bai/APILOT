import networkx as nx
G = nx.Graph()

# add nodes and edges to the graph
G.add_nodes_from([0, 1, 2])
G.add_edges_from([(0, 1), (1, 2)])

# calculate the communicability of all pairs of nodes in G
communicability = nx.communicability(G)

print(communicability)
