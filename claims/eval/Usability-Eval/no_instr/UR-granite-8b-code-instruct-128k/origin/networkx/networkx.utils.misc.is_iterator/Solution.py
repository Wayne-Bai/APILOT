import networkx as nx

def is_iterator(obj):
    return isinstance(obj, (list, tuple, dict, set, str))
