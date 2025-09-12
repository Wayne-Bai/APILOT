import networkx as nx

def partition_coverage_performance(graph, partition):
    # Calculate the size of each partition
    partition_sizes = [len(partition[partition_id]) for partition_id in partition]

    # Calculate the total number of edges in the graph
    total_edges = graph.size()

    # Calculate the coverage of the partition
    coverage = sum(partition_sizes) / total_edges

    # Calculate the performance of the partition
    performance = sum(partition_sizes) / len(graph)

    return coverage, performance
