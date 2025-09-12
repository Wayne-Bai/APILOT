import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4)])

# Get an iterator over the nodes of the graph
node_iterator = iter(G.nodes)

# Consume the iterator entirely
nodes_list = list(node_iterator)
print("Nodes list:", nodes_list)
