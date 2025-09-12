import networkx as nx
import numpy as np

def partition_performance(G, partition):
    """
    Returns the performance of a partition.
    
    The performance of a partition is the ratio of the number of intra-community edges 
    plus inter-community non-edges with the total number of potential edges.

    Parameters:
    G (networkx.Graph): The graph to compute the performance for.
    partition (list): A list of sets, each set containing the nodes in a community.

    Returns:
    float: The performance of the partition.
    """

    # Calculate the number of nodes in the graph
    num_nodes = G.number_of_nodes()

    # Calculate the total number of potential edges (assuming an undirected graph)
    total_edges = num_nodes * (num_nodes - 1) / 2

    # Initialize counters for intra-community edges and inter-community non-edges
    intra_community_edges = 0
    inter_community_non_edges = 0

    # Iterate over all pairs of nodes
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            # Check if the edge exists in the graph
            if G.has_edge(i, j):
                # Check if the nodes are in the same community
                if any(i in community and j in community for community in partition):
                    # Increment the intra-community edges counter
                    intra_community_edges += 1
            else:
                # Check if the nodes are in different communities
                if not any(i in community and j in community for community in partition):
                    # Increment the inter-community non-edges counter
                    inter_community_non_edges += 1

    # Calculate the performance
    performance = (intra_community_edges + inter_community_non_edges) / total_edges

    return performance


# Example usage:
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3)])

partition = [{0, 1, 2}, {3, 4, 5}]
print(partition_performance(G, partition))
