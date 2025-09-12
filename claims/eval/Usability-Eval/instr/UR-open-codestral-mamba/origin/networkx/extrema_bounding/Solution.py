import networkx as nx

# Create undirected graph
G = nx.Graph()

# Add edges
G.add_edge(1, 2, weight=1)
G.add_edge(1, 3, weight=5)
G.add_edge(2, 3, weight=2)
G.add_edge(2, 4, weight=3)
G.add_edge(3, 4, weight=4)
G.add_edge(4, 5, weight=2)

# Compute the extreme distance metric
extreme_distance = max([val for (u, v, val) in G.edges(data='weight')]) - min([val for (u, v, val) in G.edges(data='weight')])

print("Extreme distance metric:", extreme_distance)
