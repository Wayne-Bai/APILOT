import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)])

# Compute a minimum-weight maximal matching
matching = nx.maximum_matching(G, weight='weight')

# Print the matching
for u, v in matching.items():
    print(f'Edge {u} - {v} is in the matching')
