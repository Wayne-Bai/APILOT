import networkx as nx

def minimum_weight_maximal_matching(graph):
    # Compute a minimum-weight maximal matching
    matching = nx.max_weight_matching(graph, maxcardinality=True)
    return matching

# Example usage:
G = nx.Graph()
G.add_edge(1, 2, weight=1)
G.add_edge(1, 3, weight=2)
G.add_edge(2, 3, weight=3)
G.add_edge(3, 4, weight=4)

matching_result = minimum_weight_maximal_matching(G)
print(matching_result)
