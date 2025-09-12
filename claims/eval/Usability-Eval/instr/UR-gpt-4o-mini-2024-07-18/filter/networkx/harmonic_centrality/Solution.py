import networkx as nx

def harmonic_centrality(G):
    centrality = {}
    for node in G.nodes():
        total_distance = 0
        for other_node in G.nodes():
            if node != other_node:
                distance = nx.shortest_path_length(G, source=node, target=other_node)
                total_distance += 1 / distance if distance > 0 else 0
        centrality[node] = total_distance
    return centrality

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 1), (3, 4)])

hc = harmonic_centrality(G)
print(hc)
