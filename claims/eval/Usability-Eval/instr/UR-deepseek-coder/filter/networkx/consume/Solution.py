import networkx as nx

# Create a simple graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Define an iterator over the nodes
node_iterator = iter(G.nodes())

# Consume the iterator entirely
consumed_nodes = list(node_iterator)

# Print the consumed nodes
print(consumed_nodes)
