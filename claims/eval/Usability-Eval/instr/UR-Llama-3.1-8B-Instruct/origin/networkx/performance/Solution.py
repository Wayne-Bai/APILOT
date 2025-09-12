import networkx as nx
import numpy as np

def partition_performance(G, community):
    """
    Returns the performance of a partition.

    The performance of a partition is the ratio of the number of intra-community
    edges plus inter-community non-edges with the total number of potential edges.

    Parameters:
    G (networkx.Graph): The input graph.
    community (dict or list): A dictionary or a list where the keys are node
                              identifiers and the values are community labels.
                              In a dictionary, community labels are integers,
                              in a list, community labels are the indices.

    Returns:
    float: The performance of the partition.
    """
    
    # Get the total number of potential edges (n*(n-1)/2) where n is the number of nodes
    total_edges = G.number_of_nodes() * (G.number_of_nodes() - 1) / 2
    
    # Initialize counters for intra-community edges, inter-community non-edges
    intra_edges = 0
    inter_nonedges = 0
    
    # Iterate over all node pairs
    for i in G.nodes():
        for j in G.nodes():
            # Skip self-loops
            if i == j:
                continue
                
            # Check if the edge exists
            if G.has_edge(i, j):
                # If the edge is within a community, increment intra_edges
                if (community[i] == community[j] or
                    community[i] == community[j] if isinstance(community, dict) else
                    community[community[i]] == community[community[j]]):
                    intra_edges += 1
            else:
                # If the edge is across communities, increment inter_nonedges
                if (community[i]!= community[j] or
                    community[i]!= community[j] if isinstance(community, dict) else
                    community[community[i]]!= community[community[j]]):
                    inter_nonedges += 1
                    
    # Calculate the performance of the partition
    perf = intra_edges + inter_nonedges
    
    # Zero division error handling
    if total_edges == 0:
        return 0
    else:
        return perf / total_edges
