import networkx as nx

def partition_coverage(G, partition):
    """
    Calculate the coverage of a partition on graph G.
    
    Parameters:
    G (networkx.Graph): A NetworkX graph
    partition (list of sets): A partition of the nodes of the graph, where each set in the list represents a community
    
    Returns:
    float: The coverage of the partition.
    """
    if not isinstance(G, nx.Graph):
        raise TypeError("G must be a networkx Graph")
    if not isinstance(partition, list) or not all(isinstance(community, set) for community in partition):
        raise TypeError("partition must be a list of sets")

    intra_edges = 0
    total_edges = G.number_of_edges()

    # Calculate the number of intra-community edges
    for community in partition:
        subgraph = G.subgraph(community)
        intra_edges += subgraph.number_of_edges()

    coverage = intra_edges / total_edges
    return coverage
