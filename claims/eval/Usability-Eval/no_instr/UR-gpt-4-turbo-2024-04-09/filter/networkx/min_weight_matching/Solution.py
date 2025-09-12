import networkx as nx

# Create an example graph
G = nx.Graph()
G.add_edges_from([
    (1, 2, {'weight': 10}),
    (1, 3, {'weight': 15}),
    (2, 4, {'weight': 10}),
    (3, 4, {'weight': 10}),
    (2, 3, {'weight': 5}),
    (3, 5, {'weight': 5})
])

# Compute a minimum-weight maximal matching
matching = nx.algorithms.matching.min_weighted_matching(G, maxcardinality=False, weight='weight')

print("Minimum-weight maximal matching:", matching)
