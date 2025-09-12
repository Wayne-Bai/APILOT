import networkx as nx

# Create a directed graph
G = nx.OrderedDiGraph()

# Add nodes
G.add_nodes_from(["A", "B", "C", "D"])

# Add edges
G.add_edges_from([("A", "B"), ("B", "C"), ("C", "D")])

# Print nodes in the order they were added
print("Nodes:")
for node in G.nodes:
    print(node)

# Print edges in the order they were added
print("Edges:")
for edge in G.edges:
    print(edge)
