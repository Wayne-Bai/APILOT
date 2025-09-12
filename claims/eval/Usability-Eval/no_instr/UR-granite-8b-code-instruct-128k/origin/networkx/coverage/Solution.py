import networkx as nx

def get_coverage(partition):
    num_edges = 0
    num_intra_community_edges = 0
    for community in partition:
        graph = nx.Graph()
        graph.add_nodes_from(community)
        for node1, node2 in nx.utils.pairwise(community):
            if node1 not in partition[partition.index(community) + 1]:
                num_edges += 1
            if node2 not in partition[partition.index(community) + 1]:
                num_edges += 1
            if node1 in partition[partition.index(community) + 1]:
                num_intra_community_edges += 1
            if node2 in partition[partition.index(community) + 1]:
                num_intra_community_edges += 1
    coverage = num_intra_community_edges / num_edges
    return coverage
