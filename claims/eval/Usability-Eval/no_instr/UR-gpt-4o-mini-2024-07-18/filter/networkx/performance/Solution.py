import networkx as nx

def partition_performance(graph, partition):
    """
    Calculate the performance of a given partition of a graph.
    
    Parameters:
    graph (nx.Graph): The input graph.
    partition (dict): A dictionary where keys are node identifiers 
                      and values are community (partition) identifiers.
    
    Returns:
    float: The performance score of the partition.
    """
    intra_edges = 0
    inter_non_edges = 0
    total_potential_edges = 0

    # Count potential edges and intra-community edges
    for community in set(partition.values()):
        nodes_in_community = [node for node, comm in partition.items() if comm == community]
        total_potential_edges += len(nodes_in_community) * (len(nodes_in_community) - 1) / 2
        
        # Count edges within the community
        intra_edges += sum(1 for u in nodes_in_community for v in nodes_in_community if u < v and graph.has_edge(u, v))
        
    # Count inter-community non-edges
    for node_u in graph.nodes():
        for node_v in graph.nodes():
            if node_u != node_v and (partition[node_u] != partition[node_v]) and not graph.has_edge(node_u, node_v):
                inter_non_edges += 1

    # Performance calculation
    performance = (intra_edges + inter_non_edges) / total_potential_edges if total_potential_edges > 0 else 0
    return performance
