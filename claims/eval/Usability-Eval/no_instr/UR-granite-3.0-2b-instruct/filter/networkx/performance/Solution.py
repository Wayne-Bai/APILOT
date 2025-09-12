import networkx as nx

def partition_performance(G, partition):
    # Calculate the number of intra-community edges
    intra_community_edges = sum(G[u][v] for u, v in partition.items() if u in partition and v in partition)

    # Calculate the number of inter-community non-edges
    inter_community_non_edges = sum(G[u][v] for u in G.nodes() if u not in partition for v in G.nodes() if v not in partition)

    # Calculate the total number of potential edges
    total_potential_edges = sum(nx.number_of_edges(G))

    # Calculate the performance of the partition
    performance = (intra_community_edges + inter_community_non_edges) / total_potential_edges

    return performance
