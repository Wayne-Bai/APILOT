import networkx as nx

def is_iterator(obj):
    return hasattr(obj, '__iter__') and callable(getattr(obj, '__iter__', None))
