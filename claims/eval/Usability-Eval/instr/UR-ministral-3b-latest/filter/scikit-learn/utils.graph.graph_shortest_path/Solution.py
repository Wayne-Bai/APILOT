import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges to the graph
G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_edge("B", "D")
G.add_edge("C", "D")

# Find the shortest path between nodes
shortest_path = nx.shortest_path(G, source="A", target="D")

# Print the shortest path
print(shortest_path)
