import networkx as nx

def partition_coverage_performance(G, partition):
    coverage = 0
    performance = 0

    for community in partition:
        community_nodes = set(community)
        community_edges = set(e for e in G.edges() if e[0] in community_nodes and e[1] in community_nodes)

        coverage += len(community_nodes)
        performance += len(community_edges)

    return coverage, performance
