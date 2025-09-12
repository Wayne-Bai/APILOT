import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges with weights
G.add_edge('A', 'B', weight=1)
G.add_edge('A', 'C', weight=3)
G.add_edge('B', 'C', weight=2)
G.add_edge('B', 'D', weight=4)
G.add_edge('C', 'D', weight=5)

# Compute a minimum-weight maximal matching
matching = nx.algorithms.matching.min_weight_matching(G)

# Print the matching
for u, v in matching.edges():
    print(f"Edge {u} --{v} is in the matching")
