import networkx as nx

def partition_coverage_performance(G, partition):
    """
    Returns the coverage and performance of a partition of graph G.

    Parameters:
    G (networkx.Graph): The graph to be partitioned.
    partition (list of sets): A partition of the graph where each set contains nodes in a community.

    Returns:
    tuple: A tuple containing two floats: (coverage, performance)
    """

    # Initialize variables to compute coverage and performance
    intra_edges = 0
    inter_edges = 0
    possible_intra_edges = 0
    total_edges = G.number_of_edges()

    # Iterate over each community in the partition
    for community in partition:
        # Create a subgraph for the current community
        subgraph = G.subgraph(community)
        # Count the number of intra-community edges
        intra_edges += subgraph.number_of_edges()
        # Count the possible number of intra-community edges
        n = len(community)
        if n > 1:
            possible_intra_edges += (n * (n - 1)) / 2

    # Count the inter-community edges
    inter_edges = total_edges - intra_edges

    # Calculate coverage
    coverage = intra_edges / total_edges if total_edges > 0 else 0

    # Calculate performance
    performance = (intra_edges + (G.number_of_nodes() * (G.number_of_nodes() - 1) / 2 - possible_intra_edges)) / total_edges

    return coverage, performance

# Example usage:
G = nx.karate_club_graph()
partition = [set(G.nodes())[0:5], set(G.nodes())[5:10], set(G.nodes())[10:15], set(G.nodes())[15:]]
coverage, performance = partition_coverage_performance(G, partition)
print("Coverage:", coverage)
print("Performance:", performance)
