import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')

# Add edges to the graph
G.add_edge('A', 'B', weight=5)
G.add_edge('A', 'C', weight=3)
G.add_edge('B', 'D', weight=4)
G.add_edge('C', 'D', weight=2)

# Compute shortest paths from node A
paths = nx.shortest_path(G, source='A')

# Print the shortest paths
for node, path in paths.items():
    print(f"Shortest path from A to {node}: {path}")
