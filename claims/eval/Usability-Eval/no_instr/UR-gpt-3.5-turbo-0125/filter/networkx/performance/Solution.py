
import networkx as nx

def performance_of_partition(G, partition):
    intra_community_edges = 0
    inter_community_non_edges = 0
    total_potential_edges = 0

    for u, v in G.edges():
        if partition[u] == partition[v]:  # intra-community edge
            intra_community_edges += 1
        else:  # inter-community non-edge
            inter_community_non_edges += 1

    total_potential_edges = len(G)*(len(G)-1)/2  # total number of potential edges

    performance = (intra_community_edges + inter_community_non_edges) / total_potential_edges

    return performance
