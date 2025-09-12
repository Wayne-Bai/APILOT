import networkx as nx
def is_iterable_with_len(obj):
    return isinstance(obj, (list, tuple, str, set, dict, nx.Graph, nx.DiGraph, nx.MultiGraph, nx.MultiDiGraph))
