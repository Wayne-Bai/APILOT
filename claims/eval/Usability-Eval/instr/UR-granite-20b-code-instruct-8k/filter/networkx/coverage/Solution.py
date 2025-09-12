import networkx as nx
def partition_coverage(graph, partition):
    coverage = 0
    for community in partition:
        intracommunity_edges = 0
        for node1, node2 in graph.edges():
            if node1 in community and node2 in community:
                intracommunity_edges += 1
        coverage += intracommunity_edges / graph.number_of_edges()
    return coverage
