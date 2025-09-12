import networkx as nx

# Create a sample bipartite graph
G = nx.Graph()

# Add edges along with their weights
G.add_edge(1, 'a', weight=2)
G.add_edge(1, 'b', weight=3)
G.add_edge(2, 'a', weight=1)
G.add_edge(2, 'c', weight=4)
G.add_edge(3, 'b', weight=2)
G.add_edge(3, 'c', weight=3)

# Compute the minimum-weight maximal matching
matching = nx.max_weight_matching(G, maxcardinality=True, weight='weight')

# Output the matching result
print("Minimum-weight maximal matching:", matching)
