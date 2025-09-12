import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")

# Add edges (representing connections between nodes)
G.add_edge("A", "B", weight=2)
G.add_edge("A", "C", weight=1)
G.add_edge("B", "D", weight=3)
G.add_edge("C", "D", weight=4)

# Compute shortest path from A to D
shortest_path = nx.shortest_path(G, source="A", target="D")
print(f"Shortest path from A to D: {shortest_path}")

# Compute shortest path length from A to D
shortest_path_length = nx.shortest_path_length(G, source="A", target="D")
print(f"Shortest path length from A to D: {shortest_path_length}")
