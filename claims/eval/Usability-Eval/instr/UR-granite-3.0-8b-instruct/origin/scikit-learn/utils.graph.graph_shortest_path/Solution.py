import networkx as nx
from networkx.algorithms.shortest_paths.weighted import dijkstra_path

# Create a directed graph
G = nx.DiGraph()

# Add edges with weights
G.add_edge('A', 'B', weight=1)
G.add_edge('A', 'C', weight=3)
G.add_edge('B', 'C', weight=2)
G.add_edge('B', 'D', weight=4)
G.add_edge('C', 'D', weight=5)

# Perform a shortest-path graph search
path = dijkstra_path(G, 'A', 'D')

print(f"Shortest path from 'A' to 'D': {path}")
