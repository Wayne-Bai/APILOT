import networkx as nx

def is_iterator(obj):
    return isinstance(obj, object) and hasattr(obj, '__iter__')
