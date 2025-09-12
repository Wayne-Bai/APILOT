 
# Import necessary libraries
import networkx as nx
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Function to calculate and print extreme distance metrics
def extreme_distance_metrics(G):
    """
    Compute requested extreme distance metric of undirected graph G
    
    Parameters:
    G (nx.Graph or nx.nx_undirected): The input graph
    """
    
    # Print the longest shortest path (Diameter)
    assert isinstance(G, nx.Graph or nx.UndirectedGraph), "Input graph must be an undirected graph"
    diameter = nx.diameter(G)
    print(f"Longest shortest path (Diameter): {diameter}")
    
    # Compute and print extreme distances
    gen = nx.all_pairs_distance(G, weight=lambda u,v: 1) # Now working with simple adjacency matrix
    max_dist = 0
    min_dist = np.inf
    for u, dist in gen:
        for v, d in dist.items():
            if d > max_dist:
                max_dist = d
            if d < min_dist and d > 0:
                min_dist = d
                
    print(f"Maximum distance: {max_dist}")
    print(f"Minimum distance: {min_dist}")

# Create an example undirected graph, add edges
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)])

# Call the function to calculate and print extreme distance metrics
extreme_distance_metrics(G)
