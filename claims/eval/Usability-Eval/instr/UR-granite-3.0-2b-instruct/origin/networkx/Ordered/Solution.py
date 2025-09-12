import networkx as nx

# Create an ordered DiGraph
G = nx.DiGraph()

# Add nodes and edges in a specific order
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1, 2)
G.add_edge(2, 3)

# Print the nodes and edges in the order they were added
print("Nodes in order they were added:", G.nodes())
print("Edges in order they were added:", G.edges())
