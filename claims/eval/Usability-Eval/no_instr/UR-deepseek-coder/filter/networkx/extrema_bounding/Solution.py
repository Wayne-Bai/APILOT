import networkx as nx

def compute_extreme_distance_metric(G):
    # Compute all pairs shortest paths
    shortest_paths = dict(nx.all_pairs_shortest_path_length(G))
    
    # Initialize variables to store extreme distances
    max_distance = 0
    min_distance = float('inf')
    
    # Iterate over all pairs of nodes to find the extreme distances
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 != node2:
                distance = shortest_paths[node1].get(node2, float('inf'))
                if distance > max_distance:
                    max_distance = distance
                if distance < min_distance:
                    min_distance = distance
    
    return max_distance, min_distance

# Example usage:
# G = nx.Graph()
# G.add_edges_from([(1, 2), (2, 3), (3, 4)])
# max_dist, min_dist = compute_extreme_distance_metric(G)
# print(f"Max Distance: {max_dist}, Min Distance: {min_dist}")
