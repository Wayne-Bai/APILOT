
import networkx as nx

def calculate_coverage(partition, G):
    intra_community_edges = 0
    total_edges = len(G.edges)

    for community in partition:
        community_nodes = partition[community]
        community_subgraph = G.subgraph(community_nodes)
        intra_community_edges += len(community_subgraph.edges)

    coverage = intra_community_edges / total_edges
    return coverage

# Usage example
G = nx.karate_club_graph()
partition = {0: [0, 1, 2, 3, 4, 5], 1: [6, 7, 8, 9, 10]}
coverage = calculate_coverage(partition, G)
print("Coverage of the partition:", coverage)
