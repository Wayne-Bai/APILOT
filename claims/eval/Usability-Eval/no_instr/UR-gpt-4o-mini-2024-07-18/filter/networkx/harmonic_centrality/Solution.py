import networkx as nx

def compute_harmonic_centrality(graph):
    return nx.harmonic_centrality(graph)

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])
harmonic_centrality = compute_harmonic_centrality(G)

print(harmonic_centrality)
