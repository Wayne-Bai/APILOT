import networkx as nx

def partition_coverage(G):
    """Returns the coverage of a partition in G.

    Parameters
    ----------
    G : NetworkX graph

    Returns
    -------
    coverage : float
        The coverage of the best partition of the graph.
    """
    if G.is_directed():
        raise nx.NetworkXError("Not defined for directed graphs.")

    if G.number_of_selfloops() > 0:
        raise nx.NetworkXError("Not defined for graphs with self loops.")

    # compute the best partition
    partition = best_partition(G)

    # initialize the dict for counting the intra-community edges
    counts = dict([])
    for n in G:
        counts[partition[n]] = 0

    # count the intra-community edges
    for i, j in G.edges():
        if partition[i] == partition[j]:
            counts[partition[i]] += 1

    # compute the coverage
    cov = sum([n * (n - 1) / 2 for n in counts.values()]) / (G.number_of_edges())

    return cov
