import networkx as nx

def partition_performance(G, partition):
    """
    Calculate the performance of a partition with respect to a given graph.
    
    Parameters:
    G (networkx.Graph): The graph
    partition (dict): A dictionary representing the community partition of the nodes,
                      where the keys are nodes and the values are the community identifiers.
    
    Returns:
    float: The performance of the partition.
    """
    
    # Number of intra-community edges and inter-community non-edges
    intra_edges = 0
    inter_non_edges = 0
    total_possible_edges = G.number_of_nodes() * (G.number_of_nodes() - 1) / 2  # Combination n choose 2

    for u in G.nodes():
        for v in G.nodes():
            if u < v:  # to ensure each pair is counted once
                if partition[u] == partition[v]:  # same community
                    if G.has_edge(u, v):
                        intra_edges += 1
                else:  # different communities
                    if not G.has_edge(u, v):
                        inter_non_edges += 1

    total_edges = intra_edges + inter_non_edges
    performance = total_edges / total_possible_edges
    
    return performance
