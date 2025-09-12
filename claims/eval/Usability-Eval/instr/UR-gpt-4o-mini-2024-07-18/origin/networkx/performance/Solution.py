import networkx as nx

def partition_performance(G, partition):
    intra_edges = 0
    inter_non_edges = 0
    total_potential_edges = 0

    # Create a dictionary to hold the nodes in each community
    community_dict = {}
    for i, community in enumerate(partition):
        for node in community:
            community_dict[node] = i

    # Calculate total potential edges
    total_potential_edges = len(G.nodes) * (len(G.nodes) - 1) / 2

    # Count intra-community edges and inter-community non-edges
    for community in partition:
        for node in community:
            neighbors = set(G.neighbors(node))
            for neighbor in neighbors:
                if community_dict[neighbor] == community_dict[node]:
                    intra_edges += 1
                elif neighbor not in community_dict:
                    inter_non_edges += 1

    # Each intra-edge is counted twice (u-v and v-u), so we divide by 2
    intra_edges /= 2 

    # Resulting performance calculation
    performance = (intra_edges + inter_non_edges) / total_potential_edges if total_potential_edges > 0 else 0
    
    return performance
