import networkx as nx

def compute_extreme_distance(G):
    # Calculate shortest path length between all pairs of nodes
    # using Floyd-Warshall algorithm
    dist = dict(nx.floyd_warshall_predecessor_and_distance(G))
    
    # Calculate extreme distance metric
    extreme_dist = max(dist.values())
    
    return extreme_dist
