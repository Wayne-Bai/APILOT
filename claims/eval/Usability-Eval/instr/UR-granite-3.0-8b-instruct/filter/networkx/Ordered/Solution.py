import networkx as nx

# Create an Ordered DiGraph
G = nx.DiGraph()

# Add nodes in a specific order
G.add_nodes_from([1, 2, 3, 4, 5])

# Add edges in a specific order
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])

# Print the nodes in the order they were added
print("Nodes in order:", list(G.nodes))

# Print the edges in the order they were added
print("Edges in order:", list(G.edges))
