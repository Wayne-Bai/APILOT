import networkx as nx

# Create a graph
G = nx.Graph()

# Add some nodes and edges
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2), (2, 3)])

# Define an iterator over the nodes
node_iterator = iter(G.nodes())

# Consume the iterator entirely
consumed_nodes = list(node_iterator)

# Print the consumed nodes
print(consumed_nodes)
