import networkx as nx
import math

def compute_extreme_distance(G):
    """
    Compute extreme distance metrics for an undirected graph.
    
    Extreme distance is defined as the minimum and maximum distance
    between all pairs of nodes in the graph.
    
    Parameters:
    G (networkx.Graph): The input graph.
    
    Returns:
    tuple: A tuple containing the minimum extreme distance (xmin) and the maximum extreme distance (xmax).
    """
    
    # Initialize dictionaries to store distances
    dist_dict = nx.floyd_warshall(G)
    
    # Initialize minimum and maximum distances
    xmin = float('inf')
    xmax = float('-inf')
    
    # Iterate over all pair of nodes in the graph
    for i in G.nodes():
        for j in G.nodes():
            # If i and j are not the same node
            if i!= j:
                # Update xmin and xmax
                xmin = min(xmin, dist_dict[i][j])
                xmax = max(xmax, dist_dict[i][j])
    
    return xmin, xmax

# Create an example graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])

# Compute extreme distance
xmin, xmax = compute_extreme_distance(G)

print(f"Minimum extreme distance (xmin): {xmin}")
print(f"Maximum extreme distance (xmax): {xmax}")
