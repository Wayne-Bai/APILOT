import networkx as nx

def performance(G, partition):
    # Calculate total possible number of edges
    n = len(G)
    total_possible_edges = n * (n - 1) / 2
    
    intra_community_edges = 0
    inter_community_non_edges = 0

    # Create a dictionary to map node to community
    community_map = {}
    for idx, community in enumerate(partition):
        for node in community:
            community_map[node] = idx

    # Calculate the number of intra-community edges
    for u, v in G.edges():
        if community_map[u] == community_map[v]:
            intra_community_edges += 1

    # Calculate the number of inter-community non-edges
    for u in G.nodes():
        for v in G.nodes():
            if u != v and not G.has_edge(u, v):
                if community_map[u] != community_map[v]:
                    inter_community_non_edges += 1

    # Considering each pair (u, v) is considered twice in an undirected graph
    inter_community_non_edges /= 2

    # Calculate performance
    performance_value = (intra_community_edges + inter_community_non_edges) / total_possible_edges
    return performance_value

# Example usage
G = nx.karate_club_graph()
partition = [set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]), set([22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33])]
print(f"Performance of the partition: {performance(G, partition)}")
