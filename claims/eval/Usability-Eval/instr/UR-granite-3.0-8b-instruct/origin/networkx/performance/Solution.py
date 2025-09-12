import networkx as nx

def partition_performance(G, partition):
    intra_community_edges = 0
    inter_community_non_edges = 0
    total_potential_edges = 0

    for community in partition.values():
        intra_community_edges += nx.number_of_edges(G.subgraph(community))
        total_potential_edges += len(community) * (len(community) - 1) / 2

    for community1 in partition.values():
        for community2 in partition.values():
            if community1 != community2:
                inter_community_non_edges += len(community1) * len(community2) - nx.number_of_edges(G.subgraph(list(community1) + list(community2)))

    return (intra_community_edges + inter_community_non_edges) / total_potential_edges
