import networkx as nx

def evaluate_partition(G, partition):
    """
    Evaluates the coverage and performance of a partition of graph G.
    
    Parameters:
    G (networkx.Graph): The graph to be partitioned.
    partition (dict): A dictionary where keys are nodes and values are the partition labels.
    
    Returns:
    tuple: A tuple containing the coverage and performance metrics.
    """
    # Calculate coverage
    covered_edges = set()
    for node, part in partition.items():
        for neighbor in G.neighbors(node):
            if partition[neighbor] == part:
                covered_edges.add((min(node, neighbor), max(node, neighbor)))
    
    coverage = len(covered_edges) / G.number_of_edges()
    
    # Calculate performance (modularity)
    modularity = nx.algorithms.community.modularity(G, [set(nodes) for nodes in partition.values()])
    
    return coverage, modularity

# Example usage:
# G = nx.karate_club_graph()
# partition = {node: idx % 2 for idx, node in enumerate(G.nodes())}
# coverage, modularity = evaluate_partition(G, partition)
# print(f"Coverage: {coverage}, Modularity: {modularity}")
