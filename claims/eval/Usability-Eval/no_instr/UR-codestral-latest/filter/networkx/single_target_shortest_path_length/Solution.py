import networkx as nx

# Assume G is your graph and target is the target node
def shortest_path_lengths(G, target):
    shortest_paths = nx.single_source_shortest_path_length(G, target)
    return shortest_paths
