import networkx as nx

def partition_performance(graph, partition):
    intra_community_edges = 0
    inter_community_edges = 0
    potential_edges = 0

    for u, v in graph.edges():
        if partition[u] == partition[v]:
            intra_community_edges += 1
        else:
            inter_community_edges += 1
        potential_edges += 1

    total_edges = intra_community_edges + inter_community_edges
    potential_edges = len(graph.edges())
    performance = total_edges / potential_edges

    return performance
