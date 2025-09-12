import networkx as nx

def partition_coverage_performance(G, partition):
    """
    Returns the coverage and performance of a partition of G.

    Parameters:
    - G: A NetworkX graph
    - partition: A list where each element is a set of nodes representing a community

    Returns:
    - coverage: Fraction of edges that lie within the communities
    - performance: Fraction of correctly classified pairs (both within and between communities)
    """
    num_edges_within_communities = sum(G.subgraph(c).number_of_edges() for c in partition)
    total_edges = G.number_of_edges()
    coverage = num_edges_within_communities / total_edges if total_edges > 0 else 0

    correctly_classified_within = sum(len(c) * (len(c) - 1) // 2 for c in partition)
    correctly_classified_between = sum(
        len(c1) * len(c2) for i, c1 in enumerate(partition) for c2 in partition[i+1:]
    )

    total_pairs = len(G) * (len(G) - 1) // 2
    performance = (correctly_classified_within + correctly_classified_between) / total_pairs if total_pairs > 0 else 0

    return coverage, performance

# Example usage
G = nx.karate_club_graph()
partition = [{0, 1, 2, 3}, {4, 5, 6}, {7, 8}, {9, 10, 11, 12, 13}]
coverage, performance = partition_coverage_performance(G, partition)
print(f"Coverage: {coverage}, Performance: {performance}")
