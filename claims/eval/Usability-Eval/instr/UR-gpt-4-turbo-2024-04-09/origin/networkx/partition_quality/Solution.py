import networkx as nx

def calculate_coverage_and_performance(G, communities):
    """
    Calculate the coverage and performance of a partition of a graph.
    
    Parameters:
    G (networkx.Graph): The graph over which to calculate metrics.
    communities (list of sets): List of sets of nodes representing the communities.

    Returns:
    tuple: coverage, performance
    """
    intra_edges = 0
    total_possible_intra_edges = 0
    inter_edges = 0

    # calculate intra-community edges and possible intra-community edges
    for community in communities:
        subgraph = G.subgraph(community)
        intra_edges += subgraph.number_of_edges()
        n = len(community)
        total_possible_intra_edges += n * (n - 1) / 2

    # calculate inter-community edges
    total_edges = G.number_of_edges()
    inter_edges = total_edges - intra_edges

    # calculate coverage
    coverage = intra_edges / total_edges

    # calculate performance
    total_possible_edges = len(G) * (len(G) - 1) / 2
    performance = 1 - inter_edges / (total_possible_edges - total_possible_intra_edges)

    return coverage, performance

# Example usage:
G = nx.karate_club_graph()  # example graph
communities = [{0, 1, 2, 3, 4, 5, 6}, {7, 8, 9, 10, 11, 12, 13, 14}]  # example partition
coverage, performance = calculate_coverage_and_performance(G, communities)
print("Coverage:", coverage)
print("Performance:", performance)
