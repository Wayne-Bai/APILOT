import networkx as nx

def compute_extreme_distance(G):
    # Compute all pairs shortest paths
    shortest_paths = dict(nx.all_pairs_shortest_path_length(G))
    
    # Initialize the maximum distance to a very small number
    max_distance = -1
    
    # Iterate through all pairs of nodes to find the maximum distance
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 != node2:
                distance = shortest_paths[node1].get(node2, float('inf'))
                if distance > max_distance:
                    max_distance = distance
    
    return max_distance

# Example usage:
# G = nx.Graph()
# G.add_edges_from([(1, 2), (2, 3), (3, 4)])
# print(compute_extreme_distance(G))
