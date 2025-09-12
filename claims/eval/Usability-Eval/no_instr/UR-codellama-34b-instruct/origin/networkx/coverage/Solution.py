
import networkx as nx

def get_coverage(G, partition):
    """
    Returns the coverage of a partition. The coverage of a partition is the ratio of the number of intra-community edges to the total number of edges in the graph.

    Args:
        G (nx.Graph): The graph for which the coverage is calculated.
        partition (dict): A dictionary that maps each node to its community.

    Returns:
        float: The coverage of the partition.
    """
    total_edges = len(G.edges())
    intra_edges = 0
    for u, v in G.edges():
        if partition[u] == partition[v]:
            intra_edges += 1
    return intra_edges / total_edges
