import networkx as nx

def partition_coverage(G, partition):
    """
    Calculate the coverage of a partition on the graph G.
    
    Args:
    G (nx.Graph): A NetworkX graph.
    partition (dict): A dictionary mapping node to communities.

    Returns:
    float: The coverage of the partition.
    """
    total_edges = G.number_of_edges()
    intra_community_edges = 0

    # Create a set for each community
    communities = {}
    for node, community in partition.items():
        if community not in communities:
            communities[community] = set()
        communities[community].add(node)
    
    # Count intra-community edges
    for community, members in communities.items():
        subgraph = G.subgraph(members)
        intra_community_edges += subgraph.number_of_edges()

    coverage = intra_community_edges / total_edges if total_edges > 0 else 0
    return coverage

# Example usage
G = nx.karate_club_graph()  # Example graph
partition = {n: d['club'] for n, d in G.nodes(data=True)}
coverage = partition_coverage(G, partition)
print(f"Coverage of the partition: {coverage}")
