import networkx as nx

# Create a DiGraph
ordered_graph = nx.OrderedDiGraph()

# Add nodes in a specific order
ordered_graph.add_node("A", pos=(1, 2))
ordered_graph.add_node("B")
ordered_graph.add_node("C")

# Add edges in a specific order
ordered_graph.add_edge("A", "B", weight=1.5)
ordered_graph.add_edge("B", "C", weight=2.0)

# Print nodes in their adding order
print("Nodes in adding order:")
for node in ordered_graph.nodes(data=True):
    print(node)

# Print edges in their adding order
print("Edges in adding order:")
for edge in ordered_graph.edges(data=True):
    print(edge)
