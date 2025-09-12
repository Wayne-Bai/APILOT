import networkx as nx

def coverage(G, partition):
    intra_community_edges = 0
    total_edges = 0

    for community in set(partition.values()):
        community_nodes = [node for node, c in partition.items() if c == community]
        intra_community_edges += sum(1 for u, v in nx.edges(G) if u in community_nodes and v in community_nodes)
        total_edges += len(community_nodes)

    return intra_community_edges / total_edges
