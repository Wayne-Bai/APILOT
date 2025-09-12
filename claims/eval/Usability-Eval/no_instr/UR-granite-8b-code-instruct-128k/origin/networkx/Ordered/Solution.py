import networkx as nx

# Create a new graph
G = nx.Graph()

# Add nodes to the graph
G.add_node(1)
G.add_node(2)
G.add_node(3)

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(2, 3)

# Print the nodes in the graph, with a consistent order
print("Nodes in the graph:", list(G.nodes()))

# Print the edges in the graph, with a consistent order
print("Edges in the graph:", list(G.edges()))
