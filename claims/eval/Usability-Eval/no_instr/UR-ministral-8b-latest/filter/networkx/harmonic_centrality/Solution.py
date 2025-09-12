import networkx as nx

def compute_harmonic_centrality(G):
    harmonic_centrality = dict(nx.harmonic_centrality(G))
    return harmonic_centrality

# Example usage
if __name__ == "__main__":
    # Create a sample graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

    # Compute harmonic centrality
    h_centrality = compute_harmonic_centrality(G)

    print("Harmonic Centrality:", h_centrality)
