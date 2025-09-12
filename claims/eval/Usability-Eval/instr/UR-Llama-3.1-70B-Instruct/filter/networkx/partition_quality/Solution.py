import networkx as nx
import numpy as np

def partition_coverage_partition_performance(G, partition):
    """
    Returns the coverage and performance of a partition of G.

    Parameters:
    G (networkx.Graph): The graph for which the partition is being evaluated.
    partition (list): A list of lists where each sublist contains the nodes in a partition.

    Returns:
    tuple: A tuple containing the coverage and performance of the partition.
    """

    # Calculate the coverage
    coverage = 0
    for community in partition:
        community_edges = 0
        total_edges = 0
        for node1 in community:
            for node2 in community:
                if node1!= node2:
                    total_edges += 1
                    if G.has_edge(node1, node2):
                        community_edges += 1
        community_coverage = 0
        if total_edges > 0:
            community_coverage = community_edges / total_edges
        coverage += community_coverage / len(partition)

    # Calculate the performance (modularity)
    performance = 0
    m = G.number_of_edges()
    for community in partition:
        links_in = 0
        for node1 in community:
            for node2 in community:
                if node1!= node2:
                    if G.has_edge(node1, node2):
                        links_in += 1
        links_out = 0
        for node1 in community:
            links_out += G.degree(node1)
        links_out -= links_in
        community_performance = (links_in / (2 * m)) - ((links_out / (2 * m)) ** 2)
        performance += community_performance

    return coverage, performance


# Example usage
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5), (4, 6), (5, 6)])

partition = [[1, 2, 3], [4, 5, 6]]
coverage, performance = partition_coverage_partition_performance(G, partition)
print('Coverage:', coverage)
print('Performance (modularity):', performance)
