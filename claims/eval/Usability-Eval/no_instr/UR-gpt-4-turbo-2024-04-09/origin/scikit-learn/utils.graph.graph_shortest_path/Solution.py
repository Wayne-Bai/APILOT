import networkx as nx

# Creating a directed graph
G = nx.DiGraph()

# Adding edges along with their weights
G.add_weighted_edges_from([
    ('A', 'B', 1),
    ('B', 'C', 2),
    ('A', 'C', 4),
    ('C', 'D', 1)
])

# Compute the shortest path from A to D
path = nx.shortest_path(G, source='A', target='D', weight='weight')
print("Shortest path from A to D:", path)
