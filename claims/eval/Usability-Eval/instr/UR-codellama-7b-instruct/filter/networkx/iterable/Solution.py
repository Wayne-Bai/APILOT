
import networkx as nx

def is_iterable(obj):
    return hasattr(obj, "__len__") and not isinstance(obj, str) and not isinstance(obj, bytes)
