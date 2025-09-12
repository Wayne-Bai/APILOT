import networkx as nx

G = nx.gnp_random_graph(10, 0.5)

# Compute all-pairs shortest paths
apsp = nx.all_pairs_shortest_path(G)

# Extract the extreme distance metric
extreme_distance = max(len(apsp[u][v]) for u, v in G.edges())

print("Extreme distance:", extreme_distance)
