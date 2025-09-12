import networkx as nx

def coverage_of_partition(G, partition):
    """
    Calculate the coverage of a partition in graph G.
    
    Parameters:
    G : networkx.Graph
        The graph for which the coverage is to be calculated.
    partition : list of sets
        A list where each set contains the nodes in one community.
    
    Returns:
    float
        The coverage of the partition.
    """
    if G.number_of_edges() == 0:
        return 0.0

    # Initialize the count of intra-community edges
    intra_community_edges = 0

    # Convert partition list of sets into a list of node sets
    community_sets = [set(comm) for comm in partition]

    # Count intra-community edges
    for u, v in G.edges():
        for community in community_sets:
            if u in community and v in community:
                intra_community_edges += 1
                break

    # Calculate the total number of edges in the graph
    total_edges = G.number_of_edges()

    # Calculate and return coverage
    return intra_community_edges / total_edges

# Example usage
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3)])
partition = [{1, 2, 3}, {4, 5}]
coverage = coverage_of_partition(G, partition)
print(f"Coverage of the partition: {coverage}")
