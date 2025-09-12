import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges with weights
G.add_edge(0, 1, weight=5)
G.add_edge(0, 2, weight=3)
G.add_edge(0, 3, weight=4)
G.add_edge(1, 2, weight=7)
G.add_edge(1, 3, weight=8)
G.add_edge(2, 3, weight=2)

# Compute the minimum-weight maximal matching
min_weight_max_matching = nx.algorithms.matching.min_weight_matching(G, weight='weight')

# Print the matching
print("Minimum-weight maximal matching:", min_weight_max_matching)
