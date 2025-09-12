import networkx as nx

def compute_extreme_distance_metric(G):
    # Assuming the extreme distance metric refers to the 'diameter'
    # which is the longest shortest path in the network.
    lengths = dict(nx.all_pairs_shortest_path_length(G))
    diameter = max(max(lengths[u].values()) for u in G.nodes())
    return diameter

# Example usage:
# G = nx.Graph()
# G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])
# print(compute_extreme_distance_metric(G))
