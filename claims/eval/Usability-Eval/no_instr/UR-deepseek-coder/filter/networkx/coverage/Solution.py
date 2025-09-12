import networkx as nx

def coverage(G, partition):
    intra_community_edges = 0
    total_edges = G.number_of_edges()
    
    for community in partition:
        subgraph = G.subgraph(community)
        intra_community_edges += subgraph.number_of_edges()
    
    return intra_community_edges / total_edges

# Example usage:
# G = nx.karate_club_graph()
# partition = [{0, 1, 2, 3}, {4, 5, 6, 7}, ...]  # Example partition
# print(coverage(G, partition))
