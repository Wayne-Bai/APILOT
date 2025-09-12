import networkx as nx

# create a graph object
G = nx.Graph()

# add nodes and edges to the graph
# replace this with your own node and edge data
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])

# set the label propagation algorithm as the community detection method
nx.label_propagation_communities(G)
