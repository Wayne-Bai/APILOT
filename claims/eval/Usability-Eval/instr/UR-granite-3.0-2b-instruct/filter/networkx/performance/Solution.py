import networkx as nx

def partition_performance(G, partition):
    # Calculate the number of intra-community edges
    intra_community = 0
    for community in partition:
        intra_community += len(G.subgraph(community).edges)

    # Calculate the number of inter-community non-edges
    inter_community_non_edges = 0
    for community in partition:
        for node in community:
            for neighbor in G.neighbors(node):
                if neighbor not in community:
                    inter_community_non_edges += 1

    # Calculate the total number of potential edges
    total_potential_edges = len(G.edges)

    # Calculate the performance of the partition
    performance = (intra_community + inter_community_non_edges) / total_potential_edges

    return performance
