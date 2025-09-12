import networkx as nx

def compute_extreme_distance_metric(G, metric):
    """
    Compute the requested extreme distance metric of undirected graph G.

    Parameters:
    G (networkx.Graph): The input graph.
    metric (str): The requested distance metric. Can be 'diameter', 'eccentricity', 'radius', or 'periphery'.

    Returns:
    The requested distance metric.

    Raises:
    ValueError: If the requested metric is not supported.
    """
    if metric == 'diameter':
        return nx.diameter(G)
    elif metric == 'eccentricity':
        return max(nx.eccentricity(G).values())
    elif metric == 'radius':
        return nx.radius(G)
    elif metric == 'periphery':
        return nx.periphery(G)
    else:
        raise ValueError("Unsupported distance metric")

# Example usage:
G = nx.Graph([(1, 2), (1, 3), (2, 3), (3, 4)])
print(compute_extreme_distance_metric(G, 'diameter'))  # Output: 2
print(compute_extreme_distance_metric(G, 'eccentricity'))  # Output: 2
print(compute_extreme_distance_metric(G, 'radius'))  # Output: 1
print(compute_extreme_distance_metric(G, 'periphery'))  # Output: [1, 4]
