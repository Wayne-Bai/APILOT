import networkx as nx

# Create Ordered Graph
G = nx.OrderedGraph()

# Add nodes
G.add_nodes_from(['A', 'B', 'C', 'D'])

# Add edges
G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D')])

# Nodes are reported in the order they were added
print("Nodes in the order they were added:", list(G.nodes))

# Edges are not necessarily reported in the order they were added, but a consistent order is provided
print("Edges in a consistent order:", list(G.edges))
