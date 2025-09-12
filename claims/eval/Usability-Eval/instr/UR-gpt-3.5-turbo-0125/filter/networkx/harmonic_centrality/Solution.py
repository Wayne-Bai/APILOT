
import networkx as nx

def harmonic_centrality(G):
    centrality = {}
    for node in G.nodes():
        centrality[node] = sum(1 / len(path) for path in nx.all_shortest_paths(G, source=node).values())
    return centrality

# Example usage
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)

centrality = harmonic_centrality(G)
print(centrality)
