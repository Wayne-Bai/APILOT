import networkx as nx

# Create a sample graph
G = nx.Graph()

# Add edges with weights
G.add_edge('A', 'B', weight=1)
G.add_edge('B', 'C', weight=2)
G.add_edge('A', 'C', weight=4)
G.add_edge('C', 'D', weight=1)

# Compute shortest path from A to D
shortest_path = nx.shortest_path(G, source='A', target='D', weight='weight')

# Print the shortest path
print("Shortest path from A to D:", shortest_path)

# Compute the length of the shortest path
shortest_path_length = nx.shortest_path_length(G, source='A', target='D', weight='weight')

# Print the length of the shortest path
print("Length of shortest path from A to D:", shortest_path_length)
