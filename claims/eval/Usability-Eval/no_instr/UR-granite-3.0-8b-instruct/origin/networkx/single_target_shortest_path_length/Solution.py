import networkx as nx

def shortest_path_lengths(G, target):
    return nx.single_source_shortest_path_length(G, target)
