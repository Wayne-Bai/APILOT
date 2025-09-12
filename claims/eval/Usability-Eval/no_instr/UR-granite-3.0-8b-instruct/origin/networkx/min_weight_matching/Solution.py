import networkx as nx

def minimum_weight_maximal_matching(G):
    matching = nx.max_weight_matching(G, weight='weight')
    return matching

# Example usage:
G = nx.Graph()
G.add_edge(1, 2, weight=3)
G.add_edge(1, 3, weight=5)
G.add_edge(2, 3, weight=2)
G.add_edge(3, 4, weight=4)
G.add_edge(4, 5, weight=6)

print(minimum_weight_maximal_matching(G))
