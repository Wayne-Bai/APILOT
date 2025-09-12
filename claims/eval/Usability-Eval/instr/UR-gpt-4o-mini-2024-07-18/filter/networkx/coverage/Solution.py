import networkx as nx

def coverage_of_partition(graph, partition):
    intra_edges = 0
    total_edges = graph.number_of_edges()
    
    # Create a set for quick lookup of nodes in each community
    communities = {c: set(nodes) for c, nodes in partition.items()}
    
    # Count intra-community edges
    for u, v in graph.edges():
        for community in communities.values():
            if u in community and v in community:
                intra_edges += 1
                break
    
    # Calculate coverage
    if total_edges == 0:
        return 0  # avoid division by zero
    return intra_edges / total_edges

# Example usage:
# G = nx.Graph()
# G.add_edges_from([(1, 2), (1, 3), (2, 3), (4, 5)])
# partition = {0: [1, 2, 3], 1: [4, 5]}
# print(coverage_of_partition(G, partition))
