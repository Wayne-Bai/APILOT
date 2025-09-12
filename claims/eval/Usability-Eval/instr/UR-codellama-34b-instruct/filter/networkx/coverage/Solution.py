import networkx as nx

def get_coverage(G, partition):
    """
    Returns the coverage of a partition.

    The coverage of a partition is the ratio of the number of intra-community edges to the total number of edges in the graph.

    Parameters
    ----------
    G : NetworkX graph
        The graph on which the partition is defined.
    partition : list of sets
        A list of sets, where each set contains the nodes in a community.

    Returns
    -------
    coverage : float
        The coverage of the partition.
    """
    # Calculate the number of intra-community edges
    num_intra_edges = 0
    for community in partition:
        num_intra_edges += len(nx.subgraph(G, community).edges())

    # Calculate the total number of edges in the graph
    num_total_edges = len(G.edges())

    # Return the coverage
    return num_intra_edges / num_total_edges
