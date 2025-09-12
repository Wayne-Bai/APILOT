import networkx as nx

def performance(G, partition):
    """
    Returns the performance of a partition. The performance of a partition is the ratio of the number of intra-community edges plus inter-community non-edges with the total number of potential edges.
    """
    # Calculate the number of intra-community edges
    intra_community_edges = 0
    for community in partition:
        intra_community_edges += len(set([e for e in G.edges() if e[0] in community and e[1] in community]))
    
    # Calculate the number of inter-community non-edges
    inter_community_non_edges = 0
    for community1 in partition:
        for community2 in partition:
            if community1 != community2:
                inter_community_non_edges += len(set([e for e in G.edges() if (e[0] in community1 and e[1] in community2) or (e[0] in community2 and e[1] in community1)]))
    
    # Calculate the total number of potential edges
    total_potential_edges = len(G.nodes()) * (len(G.nodes()) - 1) / 2
    
    return (intra_community_edges + inter_community_non_edges) / total_potential_edges
