import networkx as nx

def partition_coverage(G, partition):
    intra_community_edges = 0
    total_edges = 0

    for community in partition:
        for node1 in community:
            for node2 in community:
                if G.has_edge(node1, node2):
                    intra_community_edges += 1

        total_edges += len(community) * (len(community) - 1)

    return intra_community_edges / total_edges
