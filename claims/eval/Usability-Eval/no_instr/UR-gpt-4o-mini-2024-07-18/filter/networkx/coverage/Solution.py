import networkx as nx

def coverage_of_partition(G, partition):
    """
    Returns the coverage of a partition in a graph.
    
    Parameters:
    G (networkx.Graph): The input graph.
    partition (list of sets): A partition of the graph's nodes, where each set contains nodes of a community.
    
    Returns:
    float: The coverage of the partition.
    """
    intra_community_edges = 0
    total_edges = G.number_of_edges()

    for community in partition:
        # Get all pairs of nodes in the community
        community_edges = G.edge_subgraph([(u, v) for u in community for v in community if G.has_edge(u, v)])
        intra_community_edges += community_edges.number_of_edges()

    if total_edges == 0:
        return 0.0  # Avoid division by zero

    return intra_community_edges / total_edges
