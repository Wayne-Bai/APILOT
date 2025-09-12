import networkx as nx

def get_partition_coverage_performance(G, partition):
    coverage = 0
    performance = 0

    for community in partition:
        coverage += len(community)
        performance += sum(G.degree(node) for node in community) / len(community)

    return coverage, performance
