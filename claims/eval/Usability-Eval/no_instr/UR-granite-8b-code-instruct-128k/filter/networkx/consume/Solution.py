import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5])

# Add edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)])

# Create an iterator over the nodes in the graph
node_iter = iter(G.nodes())

# Consume the iterator entirely
for node in node_iter:
    print(node)
