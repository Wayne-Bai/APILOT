import networkx as nx

def get_partition_coverage_performance(G, partition):
    """
    Calculate the coverage and performance given a graph and its partition.

    Parameters:
    G (nx.Graph): The graph.
    partition (dict): A dictionary mapping node to communities.

    Returns:
    tuple: coverage, performance
    """
    # Invert partition to get communities with list of nodes
    communities = {}
    for node, community in partition.items():
        if community not in communities:
            communities[community] = []
        communities[community].append(node)

    intra_edges = 0  # Number of edges inside communities
    inter_edges = 0  # Number of edges between communities
    total_edges = G.size()

    for community, nodes in communities.items():
        subgraph = G.subgraph(nodes)
        intra_edges += subgraph.size()
    
    inter_edges = total_edges - intra_edges
    coverage = intra_edges / total_edges
    performance = 1 - (inter_edges / total_edges)

    return coverage, performance

# Example usage:
G = nx.karate_club_graph()
partition = {n: n % 2 for n in G.nodes()}  # Example partitioning by mod 2
coverage, performance = get_partition_coverage_performance(G, partition)
print("Coverage:", coverage)
print("Performance:", performance)
