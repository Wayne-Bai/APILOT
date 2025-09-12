import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes
G.add_node("A")
G.add_node("B")
G.add_node("C")

# Add edges
G.add_edge("A", "B")
G.add_edge("B", "C")

# Consume the iterator entirely
for node in G.nodes:
    print(node)
