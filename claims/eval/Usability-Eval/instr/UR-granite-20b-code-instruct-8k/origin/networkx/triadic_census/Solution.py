import networkx as nx

def get_triadic_census(graph):
    triads = nx.triadic_census(graph)
    return triads