import networkx as nx

# Create a graph
G = nx.Graph()

# Add weighted edges
G.add_edge('A', 'B', weight=3)
G.add_edge('B', 'C', weight=1)
G.add_edge('C', 'D', weight=4)
G.add_edge('D', 'A', weight=2)
G.add_edge('B', 'D', weight=5)

# Compute the minimum weight maximal matching
matching = nx.algorithms.matching.min_weighted_matching(G, maxcardinality=False)

print("Minimum-weight maximal matching:")
print(matching)
