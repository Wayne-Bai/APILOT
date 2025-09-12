import networkx as nx

def harmonic_centrality(G, v):
    """
    Compute the harmonic centrality for a node v in graph G.
    
    Parameters:
    G (networkx.Graph): The graph.
    v (node): The node for which harmonic centrality is to be computed.
    
    Returns:
    float: The harmonic centrality of node v.
    """
    total_distance = 0.0
    for node in G.nodes():
        if node != v:
            try:
                shortest_path_length = nx.shortest_path_length(G, source=v, target=node)
                if shortest_path_length > 0:
                    total_distance += 1.0 / shortest_path_length
            except nx.NetworkXNoPath:
                # If there is no path between v and node, we ignore this node
                pass
    return total_distance

# Example usage:
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])
node = 2
centrality = harmonic_centrality(G, node)
print(f"Harmonic centrality of node {node}: {centrality}")
