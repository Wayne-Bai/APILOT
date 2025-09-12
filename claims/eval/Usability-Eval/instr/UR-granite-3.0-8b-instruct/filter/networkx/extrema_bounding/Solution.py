import networkx as nx

def compute_extreme_distance_metric(G):
    # Compute the shortest path between all pairs of nodes
    shortest_paths = dict(nx.all_pairs_dijkstra_path(G))

    # Compute the maximum distance between any two nodes
    max_distance = max(len(path) for path in shortest_paths.values())

    return max_distance

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)])
print(compute_extreme_distance_metric(G))
