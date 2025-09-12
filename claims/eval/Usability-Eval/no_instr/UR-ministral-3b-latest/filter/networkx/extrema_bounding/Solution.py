import networkx as nx

def extreme_distance_metric(graph, start_node):
    G = nx.undirected_graph(graph)
    extremes = nx.algorithms.distance_pairs(G, threshold=None, weight=None)
    max_distance = max(max(d) for d in extremes)

    return max_distance
