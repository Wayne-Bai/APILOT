import networkx as nx

def calculate_minimum_weight_max_matching(G):
    # Find the maximum weight matching using the亨gin algorithm
    matching = nx.algorithms.matching.hungarian(G)
    max_weight = sum(G[u][v].get('weight', 1) for u, v in matching)
    return matching, max_weight

# Let's create a sample graph
G = nx.Graph()
G.add_weighted_edges_from([(1, 2, 1), (1, 3, 2), (2, 3, 3), (3, 4, 1), (4, 5, 4), (5, 6, 2)])
matching, max_weight = calculate_minimum_weight_max_matching(G)
print("Maximum weight matching:", matching)
print("Maximum weight:", max_weight)
