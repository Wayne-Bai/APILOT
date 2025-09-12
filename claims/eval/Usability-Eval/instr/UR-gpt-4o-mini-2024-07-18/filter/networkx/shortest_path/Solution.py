import networkx as nx

# Create a sample directed graph
G = nx.DiGraph()

# Add edges along with their weights
G.add_edge('A', 'B', weight=1)
G.add_edge('B', 'C', weight=2)
G.add_edge('A', 'C', weight=4)
G.add_edge('C', 'D', weight=1)

# Compute the shortest path from node 'A' to node 'D'
shortest_path = nx.shortest_path(G, source='A', target='D', weight='weight')
shortest_path_length = nx.shortest_path_length(G, source='A', target='D', weight='weight')

print("Shortest path from A to D:", shortest_path)
print("Length of shortest path from A to D:", shortest_path_length)
