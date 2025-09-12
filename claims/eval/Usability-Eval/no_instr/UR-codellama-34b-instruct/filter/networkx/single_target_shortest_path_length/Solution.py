import networkx as nx

def get_shortest_paths(graph, source):
    return list(nx.all_shortest_paths(graph, source))
