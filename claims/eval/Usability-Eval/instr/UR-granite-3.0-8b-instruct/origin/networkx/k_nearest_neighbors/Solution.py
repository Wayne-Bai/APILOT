import networkx as nx

def average_degree_connectivity(G):
    """
    Compute the average degree connectivity of a graph.

    Parameters:
    G (NetworkX graph): The graph to compute the average degree connectivity for.

    Returns:
    float: The average degree connectivity of the graph.
    """
    degrees = nx.degree(G)
    k_values = sorted(set(degrees.values()))
    avg_degree_connectivity = 0

    for k in k_values:
        neighbors = set()
        for node in G.nodes():
            if degrees[node] == k:
                neighbors.update(G.neighbors(node))
        avg_degree_connectivity += len(neighbors) / len(G.nodes())

    return avg_degree_connectivity / len(k_values)
