import networkx as nx

def coverage_and_performance(G, partition):
    """
    Calculate the coverage and performance of a partition of the graph G.

    Parameters:
    G (nx.Graph): The input graph.
    partition (list of sets): A partition of the graph's nodes.

    Returns:
    tuple: A tuple containing coverage and performance scores.
    """
    total_edges = G.number_of_edges()
    covered_edges = 0
    
    for subset in partition:
        subgraph = G.subgraph(subset)
        covered_edges += subgraph.number_of_edges()

    coverage = covered_edges / total_edges if total_edges > 0 else 0
    performance = len(partition) / G.number_of_nodes() if G.number_of_nodes() > 0 else 0

    return coverage, performance
