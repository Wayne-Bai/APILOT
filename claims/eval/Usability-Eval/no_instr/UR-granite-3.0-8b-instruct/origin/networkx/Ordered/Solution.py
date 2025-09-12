import networkx as nx

# Create an Ordered DiGraph
G = nx.OrderedDiGraph()

# Add nodes
G.add_node(1)
G.add_node(2)
G.add_node(3)

# Add edges
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(1, 3)

# Print nodes and edges in order
print("Nodes:", G.nodes)
print("Edges:", G.edges)
