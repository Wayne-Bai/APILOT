import networkx as nx
import numpy as np

def partition_coverage(G, partition):
    """
    Returns the coverage of a partition.
    
    The coverage of a partition is the ratio of the number of intra-community edges
    to the total number of edges in the graph.
    
    Parameters
    ----------
    G : NetworkX graph
        The graph on which the partition is defined.
    partition : list or tuple
        The partition of the network.

    Returns
    -------
    coverage : float
        The coverage of the partition.
    """
    intra_community_edges = 0
    for community in partition:
        community_subgraph = G.subgraph(community)
        intra_community_edges += community_subgraph.number_of_edges()
    
    total_edges = G.number_of_edges()
    
    coverage = intra_community_edges / total_edges
    return coverage

# Example usage
if __name__ == "__main__":
    # Create a graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 6), (5, 6)])

    # Define a partition
    partition = [[1, 2, 3], [4, 5, 6]]

    # Calculate the coverage of the partition
    coverage = partition_coverage(G, partition)
    print("Coverage of the partition:", coverage)
