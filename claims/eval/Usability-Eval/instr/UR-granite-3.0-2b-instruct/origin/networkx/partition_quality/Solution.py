import networkx as nx

def partition_coverage_performance(G):
    # Generate all possible partitions of G
    partitions = list(nx.all_partitions(G))

    # Initialize lists to store coverage and performance
    coverage = []
    performance = []

    # Calculate coverage and performance for each partition
    for partition in partitions:
        # Calculate coverage as the sum of the degrees of nodes in the partition
        coverage.append(sum(G.degree(node) for node in partition))

        # Calculate performance as the sum of the reciprocals of the degrees of nodes in the partition
        performance.append(sum(1 / G.degree(node) for node in partition))

    return coverage, performance
