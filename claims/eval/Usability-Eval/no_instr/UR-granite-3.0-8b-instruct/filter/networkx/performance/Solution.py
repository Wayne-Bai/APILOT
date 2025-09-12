import networkx as nx

def calculate_performance(G, partition):
    intra_community_edges = 0
    inter_community_non_edges = 0
    total_potential_edges = 0

    for community in partition:
        for node in community:
            total_potential_edges += len(G.neighbors(node)) - 1
            intra_community_edges += sum(G.neighbors(node) in community for node in community)
            inter_community_non_edges += len(set(G.neighbors(node)) & set(community)) - intra_community_edges

    performance = (intra_community_edges + inter_community_non_edges) / total_potential_edges
    return performance
