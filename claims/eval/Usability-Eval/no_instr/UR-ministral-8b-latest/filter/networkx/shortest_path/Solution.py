import networkx as nx
import numpy as np

# Example graph
G = nx.Graph()
G.add_edge('A', 'B', weight=1)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'D', weight=1)
G.add_edge('C', 'D', weight=1)

# Define the source and target nodes for shortest path
source = 'A'
target = 'D'

# Compute the shortest path
try:
    shortest_path = nx.shortest_path(G, source=source, target=target, weight='weight')
    print(f"Shortest path from {source} to {target}: {shortest_path}")
    print(f"Shortest path length: {nx.shortest_path_length(G, source=source, target=target, weight='weight')}")
except nx.NetworkXNoPath:
    print(f"No path found from {source} to {target}")
