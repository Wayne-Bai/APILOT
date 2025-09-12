import networkx as nx

def compute_harmonic_centrality(G):
    """
    Computes the harmonic centrality for nodes in a graph G.
    
    Parameters:
    G : NetworkX graph
        A graph for which harmonic centrality is to be computed.

    Returns:
    dict
        A dictionary with nodes as keys and harmonic centrality as values.
    """
    # Compute harmonic centrality
    harmonic_centrality = nx.harmonic_centrality(G)
    return harmonic_centrality

# Example usage:
if __name__ == "__main__":
    # Create a sample graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)])
    
    # Calculate harmonic centrality
    centrality = compute_harmonic_centrality(G)
    
    # Print the results
    for node, value in centrality.items():
        print(f"Node {node}: Harmonic Centrality = {value}")
