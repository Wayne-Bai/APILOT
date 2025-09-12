import networkx as nx

def performance(G, partition):
    """
    Calculate the performance of a partition.
    
    Parameters:
    G (networkx.Graph): The graph.
    partition (dict): A dictionary where keys are nodes and values are the community IDs.
    
    Returns:
    float: The performance of the partition.
    """
    intra_edges = 0
    inter_non_edges = 0
    total_edges = G.number_of_edges()
    total_possible_edges = G.number_of_nodes() * (G.number_of_nodes() - 1) / 2
    
    for u, v in G.edges():
        if partition[u] == partition[v]:
            intra_edges += 1
    
    for u in G.nodes():
        for v in G.nodes():
            if u != v and not G.has_edge(u, v):
                if partition[u] != partition[v]:
                    inter_non_edges += 1
    
    performance_score = (intra_edges + inter_non_edges) / total_possible_edges
    return performance_score

# Example usage:
# G = nx.karate_club_graph()
# partition = {node: G.nodes[node]['club'] for node in G.nodes()}
# print(performance(G, partition))
