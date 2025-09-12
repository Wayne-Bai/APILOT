import networkx as nx

def extreme_distance_metric(G):
    # Calculate the maximum distance between any two nodes
    max_distance = 0
    for node1 in G.nodes():
        lengths = nx.single_source_shortest_path_length(G, node1)
        for node2, distance in lengths.items():
            if distance > max_distance:
                max_distance = distance
                
    return max_distance

# Example of usage
if __name__ == "__main__":
    # Create an undirected graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (1, 4)])
    
    # Compute the extreme distance metric
    metric = extreme_distance_metric(G)
    print("Extreme distance metric:", metric)
