import networkx as nx

def minimum_weight_maximal_matching(G):
    # Compute a minimum-weight maximal matching
    matching = nx.max_weight_matching(G, maxcardinality=True, weight='weight')
    
    return matching

# Example usage:
G = nx.Graph()
G.add_edge('A', 'B', weight=2)
G.add_edge('B', 'C', weight=5)
G.add_edge('A', 'C', weight=1)

matching = minimum_weight_maximal_matching(G)
print("Minimum-weight maximal matching:", matching)
