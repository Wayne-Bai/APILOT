import networkx as nx

def compute_extreme_distance_metric(G):
    # Compute shortest path between all pairs of nodes
    shortest_paths = dict(nx.all_pairs_shortest_path_length(G))

    # Compute the maximum shortest path length
    max_distance = max(shortest_paths.values())

    return max_distance
