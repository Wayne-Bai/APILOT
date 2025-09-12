import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(5, 1)

# Calculate shortest path from node 1 to node 5
shortest_path = nx.shortest_path(G, source=1, target=5)

# Print the resulting shortest path
print("Shortest path from node 1 to node 5:", shortest_path)
