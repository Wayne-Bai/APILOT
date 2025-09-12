import networkx as nx

def harmonic_centrality(G):
    H = {}
    for u in G.nodes():
        H[u] = 0  # Initialize harmonic centrality to zero for each node
        for v in G.nodes():
            if u != v:
                try:
                    shortest_path_length = nx.shortest_path_length(G, source=u, target=v)
                    if shortest_path_length > 0:
                        H[u] += 1 / shortest_path_length
                except nx.NetworkXNoPath:
                    continue  # If there is no path, simply skip
    return H

# Example usage:
G = nx.Graph()

# Add some edges
edges = [(0, 1), (1, 2), (1, 3), (3, 4)]
G.add_edges_from(edges)

# Compute harmonic centrality
hc = harmonic_centrality(G)
print(hc)
