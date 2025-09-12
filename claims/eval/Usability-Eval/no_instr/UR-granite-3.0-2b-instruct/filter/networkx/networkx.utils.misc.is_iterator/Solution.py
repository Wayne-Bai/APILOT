import networkx as nx

def is_iterator(obj):
    return isinstance(obj, (nx.Graph, nx.DiGraph, nx.MultiGraph, nx.MultDiGraph))
