import networkx as nx
from collections import defaultdict

def partition_coverage(graph, partition):
    """
    Compute the coverage of a partition in a graph.

    The coverage of a partition is the ratio of the number of intra-community edges
    to the total number of edges in the graph.

    Parameters
    ----------
    graph : NetworkX Graph
        The graph where the partition is applied.
    partition : list of lists
        A list of communities, where each community is a list of nodes.

    Returns
    -------
    float
        The coverage of the partition in the graph.
    """
    # Initialize counters for intra-community edges and total edges
    intra_community_edges = 0
    total_edges = 0

    # Create a dictionary to store the community of each node
    node_community = defaultdict(int)
    for i, community in enumerate(partition):
        for node in community:
            node_community[node] = i

    # Iterate over all edges in the graph
    for u, v in graph.edges():
        total_edges += 1
        # Check if the edge is intra-community
        if node_community[u] == node_community[v]:
            intra_community_edges += 1

    # Calculate and return the coverage of the partition
    if total_edges == 0:
        return 0
    else:
        return intra_community_edges / total_edges


# Example usage:
if __name__ == "__main__":
    # Create a sample graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 6)])

    # Define a partition of the graph
    partition = [[1, 2, 3], [4, 5, 6]]

    # Compute the coverage of the partition
    coverage = partition_coverage(G, partition)

    print("Coverage of the partition:", coverage)
