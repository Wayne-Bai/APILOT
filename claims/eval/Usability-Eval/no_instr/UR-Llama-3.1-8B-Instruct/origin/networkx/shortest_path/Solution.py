# Import necessary libraries
import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")

# Add edges with weights
G.add_edge("A", "B", weight=2)
G.add_edge("A", "C", weight=4)
G.add_edge("B", "C", weight=1)
G.add_edge("B", "D", weight=7)
G.add_edge("C", "D", weight=3)
G.add_edge("C", "E", weight=5)
G.add_edge("D", "E", weight=6)

# Compute shortest paths
shortest_path_length = nx.shortest_path_length(G, "A")  # All shortest path lengths
shortest_path = nx.shortest_path(G, source="A")  # Shortest path from A to all other nodes

# Print the results
print("Shortest path length from A to other nodes:")
for node in G.nodes:
    if node!= "A":
        print(f"A -> {node}: {shortest_path_length['A'][node]}")

print(f"\nShortest path from A to other nodes: {shortest_path}")
