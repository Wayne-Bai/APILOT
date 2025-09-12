import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges with weights
G.add_edge('A', 'B', weight=7)
G.add_edge('A', 'C', weight=9)
G.add_edge('B', 'C', weight=14)
G.add_edge('B', 'D', weight=10)
G.add_edge('C', 'D', weight=15)

# Compute shortest paths
shortest_paths = nx.all_shortest_paths(G, source='A', target='D')

# Print the shortest paths
for path in shortest_paths:
    print(path)
