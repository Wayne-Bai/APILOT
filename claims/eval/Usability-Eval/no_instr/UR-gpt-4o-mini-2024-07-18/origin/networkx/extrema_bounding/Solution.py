import networkx as nx

def extreme_distance_metric(G):
    # Get all pairs of nodes
    all_pairs_shortest_paths = dict(nx.all_pairs_shortest_path_length(G))
    
    # Initialize extremal distances
    min_distance = float('inf')
    max_distance = float('-inf')
    
    # Loop through distances to find min and max
    for source in all_pairs_shortest_paths:
        for target, distance in all_pairs_shortest_paths[source].items():
            if distance < min_distance:
                min_distance = distance
            if distance > max_distance:
                max_distance = distance
                
    return min_distance, max_distance

# Example usage:
# G = nx.Graph([(1, 2), (2, 3), (3, 4), (1, 4)]) # Create an example graph
# min_dist, max_dist = extreme_distance_metric(G)
# print(f"Minimum distance: {min_dist}, Maximum distance: {max_dist}")
