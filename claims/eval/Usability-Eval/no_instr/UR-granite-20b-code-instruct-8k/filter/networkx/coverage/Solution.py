import networkx as nx
def partition_coverage(graph, partition):
    """
    Returns the coverage of a partition.
    The coverage of a partition is the ratio of the number of intra-community edges
    to the total number of edges in the graph.
    """
    if not isinstance(graph, nx.Graph):
        raise TypeError("graph must be a NetworkX graph")
    if not isinstance(partition, dict):
        raise TypeError("partition must be a dictionary")
    intracommities = 0
    for community in partition.values():
        for node_a in community:
            for node_b in community:
                if node_a != node_b and graph.has_edge(node_a, node_b):
                    intracommities += 1
    return intracommities / graph.size()
