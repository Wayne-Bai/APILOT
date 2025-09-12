import networkx as nx

def partition_performance(G, partition):
    """
    Returns the performance of a partition.
    
    The performance of a partition is the ratio of the number of intra-community edges plus inter-community non-edges 
    with the total number of potential edges.

    Parameters
    ----------
    G : networkx.Graph
        The graph to calculate the partition performance for.
    partition : dict
        A dictionary mapping each node in G to its community ID.

    Returns
    -------
    float
        The performance of the partition.
    """
    num_intra_edges = 0
    num_inter_non_edges = 0
    total_nodes = len(G)
    total_potential_edges = total_nodes * (total_nodes - 1) / 2

    for u in G.nodes:
        for v in G.nodes:
            if u!= v:
                if partition[u] == partition[v]:
                    if G.has_edge(u, v):
                        num_intra_edges += 1
                else:
                    if not G.has_edge(u, v):
                        num_inter_non_edges += 1

    performance = (num_intra_edges + num_inter_non_edges) / total_potential_edges
    return performance

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)])

partition = {1: 0, 2: 0, 3: 0, 4: 1, 5: 1}

print(partition_performance(G, partition))
