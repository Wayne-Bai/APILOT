import networkx as nx

# Create a graph
G = nx.Graph()

# Add some edges to the graph
G.add_edge('A', 'B', weight=1)
G.add_edge('B', 'C', weight=3)
G.add_edge('C', 'D', weight=4)
G.add_edge('A', 'D', weight=10)

# Compute shortest path from A to D
path = nx.dijkstra_path(G, source='A', target='D', weight='weight')
print("Shortest path from A to D:", path)
