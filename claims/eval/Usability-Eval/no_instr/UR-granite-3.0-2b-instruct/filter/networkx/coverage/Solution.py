import networkx as nx

def coverage(graph, partition):
    intra_community_edges = 0
    total_edges = 0

    for community in partition:
        intra_community_edges += sum(graph.subgraph(community).edges())
        total_edges += len(graph.edges())

    return intra_community_edges / total_edges if total_edges > 0 else 0
