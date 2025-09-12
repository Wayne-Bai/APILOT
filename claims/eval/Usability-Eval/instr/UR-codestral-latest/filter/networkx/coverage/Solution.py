import networkx as nx

def partition_coverage(G, partition):
    # Total number of edges in the graph
    total_edges = G.number_of_edges()

    # Count the number of intra-community edges
    intra_community_edges = 0
    for community in partition:
        subgraph = G.subgraph(community)
        intra_community_edges += subgraph.number_of_edges()

    # Coverage is the ratio of intra-community edges to total edges
    coverage = intra_community_edges / total_edges
    return coverage
