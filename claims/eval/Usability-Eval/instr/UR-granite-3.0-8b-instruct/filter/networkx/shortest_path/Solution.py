import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
G.add_edge('A', 'B', weight=7)
G.add_edge('A', 'C', weight=9)
G.add_edge('A', 'F', weight=14)
G.add_edge('B', 'C', weight=10)
G.add_edge('B', 'D', weight=15)
G.add_edge('C', 'D', weight=11)
G.add_edge('C', 'F', weight=2)
G.add_edge('D', 'E', weight=6)
G.add_edge('E', 'F', weight=9)

# Compute shortest paths from 'A' to all other nodes
shortest_paths = nx.single_source_dijkstra(G, 'A')

# Print the shortest paths
for node, path in shortest_paths.items():
    if node != 'A':
        print(f"Shortest path from A to {node}: {path}")
