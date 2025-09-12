import networkx as nx

def evaluate_partition(G, partition):
    """
    Evaluates the coverage and performance of a partition of graph G.

    Parameters:
    G (networkx.Graph): The graph to be partitioned.
    partition (dict): A dictionary where keys are nodes and values are the partition labels.

    Returns:
    coverage (float): The fraction of edges that are within the same partition.
    performance (float): The modularity of the partition.
    """
    # Calculate coverage
    intra_edges = 0
    total_edges = G.number_of_edges()
    
    for u, v in G.edges():
        if partition[u] == partition[v]:
            intra_edges += 1
    
    coverage = intra_edges / total_edges
    
    # Calculate performance (modularity)
    modularity = nx.algorithms.community.modularity(G, [set(nodes) for nodes in partition.values()])
    
    return coverage, modularity

# Example usage:
# G = nx.karate_club_graph()
# partition = {node: idx % 2 for idx, node in enumerate(G.nodes())}
# coverage, performance = evaluate_partition(G, partition)
# print(f"Coverage: {coverage}, Performance: {performance}")
