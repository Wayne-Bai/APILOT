import networkx as nx

def min_weight_max_matching(G):
    M = nx.max_weight_matching(G)
    weight = sum(d for u, v, d in G.edges(data=True) if (u, v) in M)
    return weight

# Example usage:
G = nx.Graph()
G.add_edge('A', 'B', weight=3)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'C', weight=4)
G.add_edge('B', 'D', weight=1)
G.add_edge('C', 'D', weight=5)

min_weight_max_matching(G)
