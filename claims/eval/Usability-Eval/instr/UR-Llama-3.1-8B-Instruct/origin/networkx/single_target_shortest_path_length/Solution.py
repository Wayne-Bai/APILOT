import networkx as nx

# Create an undirected graph
G = nx.Graph()

# Add nodes
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')

# Add edges with weights
G.add_edge('A', 'B', weight=2)
G.add_edge('B', 'C', weight=3)
G.add_edge('A', 'C', weight=4)
G.add_edge('A', 'D', weight=8)
G.add_edge('C', 'D', weight=1)

# Compute shortest path lengths to 'D' from all reachable nodes
try:
    shortest_distances = nx.shortest_path_length(G, target='D')
    print(shortest_distances)
except nx.NetworkXNoPath:
    print("There's no path from any node to 'D'")
