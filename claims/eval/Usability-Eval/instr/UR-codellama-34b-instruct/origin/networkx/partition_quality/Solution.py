
import networkx as nx

def get_coverage(G, partition):
    """
    Calculates the coverage of a partition of G.

    Parameters:
        G (nx.Graph): The graph to be partitioned.
        partition (list): A list of lists containing the nodes in each subset.

    Returns:
        coverage (float): The coverage of the partition.
    """
    # Calculate the number of edges within each subset
    num_subset_edges = 0
    for subset in partition:
        num_subset_edges += len(list(nx.subgraph(G, subset).edges()))

    # Calculate the total number of edges in G
    total_num_edges = len(list(G.edges()))

    # Calculate the coverage of the partition
    coverage = num_subset_edges / total_num_edges

    return coverage
