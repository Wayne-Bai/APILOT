import networkx as nx

def coverage(partition):
    G = nx.Graph()
    G.add_edges_from(partition)

    intra_community_edges = 0
    total_edges = 0

    for community in partition:
        intra_community_edges += len(G.subgraph(community).edges())
        total_edges += len(G.edges())

    return intra_community_edges / total_edges
